import usb.core
import usb.util


class USBReader:
    def __init__(self, vendor_id, product_id):
        self.vendor_id = vendor_id
        self.product_id = product_id
        self.device = None

        pass

    def find_device(self):
        self.device = usb.core.find(idVendor=self.vendor_id, idProduct=self.product_id)
        if self.device is None:
            raise ValueError("Device not found.")
        pass

    def setup_device(self):
        if self.device is not None:
            self.device.set_configuration()

            cfg = self.device.get_active_configuration()
            interface_number = cfg[(0, 0)].bInterfaceNumber
            usb.util.claim_interface(self.device, interface_number)

        pass

    def read_rfid_data(self):
        if self.device is not None:
            endpoint = self.device[0][(0, 0)][0]
            rfid_data = ''

            try:
                while True:
                    data = self.device.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize)

                    rfid_data += data
            except KeyboardInterrupt:
                pass
            return rfid_data
        

if __name__ == '__main__':
    VENDOR_ID = 0x16c0
    PRODUCT_ID = 0x27db

    try:
        print("hello")
        usb_reader = USBReader(VENDOR_ID, PRODUCT_ID)
        usb_reader.find_device()
        usb_reader.setup_device()

        #rfid_data = usb_reader.read_rfid_data()
        #print("RFID data : ", rfid_data)
    except Exception as e:
        print(f"An Error occured : {e}")