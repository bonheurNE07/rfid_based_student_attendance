import subprocess

def usb_devices_infos()->list:
    """
    Get informations about all USB devices connected to the Raspberry Pi using the lsub command.

    Returns:
        List : A list of dictionaries containing information about each USB device.
               Each dictionary includes keys for 'Vendors ID','Product ID' and 'Descriprion of the device'.
    """
    usb_info = []
    try:
        # run the linux command 'lsub' to list USB devices connected and return the data as text
        lsusb_outuput = subprocess.run(['lsusb'], capture_output=True, text=True, check=True)
        lines = lsusb_outuput.stdout.split('\n')
        print(lsusb_outuput)
        for line in lines:
            if line:
                parts = line.split()
                # code to extract vendor ID, product ID and Description of the device
                vendor_id = parts[5][:4]
                product_id = parts[5][5:9]
                device_description = ''.join(parts[6:])

                # append all these data values on our usb device list
                usb_info.append({
                    'Vendor ID':vendor_id,
                    'Product ID':product_id,
                    'Description':device_description
                })
    
    except subprocess.CalledProcessError as ProcError:
        print(f"Process Error running lsub command: {ProcError}")
    except Exception as e:
        print(f"An Error occured: {e}")
    return usb_info

# Get and print All USB devices connected to the Raspi
usb_devices = usb_devices_infos()
for device in usb_devices:
    print(device)