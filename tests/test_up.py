import time
from evdev import InputDevice, list_devices, ecodes

class RFIDReader:
    """A class for reading RFID data from an HID device."""

    def __init__(self, vendor_id, product_id):
        """
        Initialize the RFIDReader.

        Parameters:
        - vendor_id (int): Vendor ID of the HID device.
        - product_id (int): Product ID of the HID device.
        """
        self.vendor_id = vendor_id
        self.product_id = product_id
        self.device = None
        self.key_mapping = {
            ecodes.KEY_0: '0',
            ecodes.KEY_1: '1',
            ecodes.KEY_2: '2',
            ecodes.KEY_3: '3',
            ecodes.KEY_4: '4',
            ecodes.KEY_5: '5',
            ecodes.KEY_6: '6',
            ecodes.KEY_7: '7',
            ecodes.KEY_8: '8',
            ecodes.KEY_9: '9',
            # Add more mappings for other keys as needed
        }
        self.rfid_data = ""
        self.data_list = []
        self.return_data = ""
        self.final_data = []

    def open_device(self)-> bool:
        """
        Open the RFID Reader HID device with the specified vendor and product IDs.

        Returns:
        - bool: True if device is opened successfully, False otherwise.
        """
        devices = [InputDevice(dev) for dev in list_devices()]
        # print(devices)
        for device in devices:
            if device.info.vendor == self.vendor_id and device.info.product == self.product_id:
                self.device = device
                print("RFID event device opened:", device)
                return True
        print("RFID event device not found.")
        return False

    def read_rfid_data(self)-> list:
        """
        Read RFID data from the RFID Reader HID device.

        Returns:
        - list: Updated list of RFID card sacnned number.
        """
        if not self.device:
            print("RFID device not opened.")
            return None

        print("Reading RFID data...")
        try:
            for event in self.device.read_loop():
                if event.type == ecodes.EV_KEY and event.value == 1:
                    key_code = event.code
                    if key_code in self.key_mapping:
                        key = self.key_mapping[key_code]
                        if len(self.rfid_data) <= 10:
                            self.rfid_data += key
                            if len(self.rfid_data) == 10:
                                self.data_list.append(self.rfid_data)
                                self.return_data = self.rfid_data
                                self.final_data = [self.return_data, self.data_list]

                                self.rfid_data = ""
                                return self.final_data  # Return updated list when length changes
                            else:
                                self.return_data = ""
                                self.final_data = []
                                pass
                        else:
                            self.rfid_data = ""  # Reset RFID data string if length exceeds 10
        except KeyboardInterrupt:
            pass

    def close_device(self):
        """Close the HID device."""
        if self.device:
            self.device.close()
            print("RFID event device closed.")

# Example usage:
if __name__ == "__main__":
    vendor_id = 0x16c0
    product_id = 0x27db
    reader = RFIDReader(vendor_id, product_id)

    if reader.open_device():
        try:
            while True:
                data = reader.read_rfid_data()
                if data:
                    print("Received RFID data:", data)
        finally:
            reader.close_device()
