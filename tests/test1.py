import hid

# Vendor and Product IDs of your HID device (replace with actual IDs)
vendor_id = 0x16c0
product_id = 0x27db

def find_hid_device(vendor_id, product_id):
    for device_info in hid.enumerate(vendor_id, product_id):
        if device_info['vendor_id'] == vendor_id and device_info['product_id'] == product_id:
            return device_info
    return None

try:
    device_info = find_hid_device(vendor_id, product_id)
    if device_info is None:
        print("HID device not found.")
        exit()

    device_path = device_info['path']
    print("HID device found at path:", device_path)

    dev = hid.device(vendor_id, product_id)
    dev.open_path(device_path)
    print("HID device opened successfully.")

    try:
        print("Reading HID data...")
        while True:
            data = dev.read(64)  # Read data from the HID device
            if data:
                # Process and print the received data
                print("Received HID data:", data)
    except KeyboardInterrupt:
        print("Keyboard interrupt. Exiting.")
    finally:
        dev.close()
except Exception as e:
    print("Error:", e)
