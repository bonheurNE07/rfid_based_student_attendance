import time
from evdev import InputDevice, list_devices, ecodes

key_mapping = {
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

def find_rfid_event_device():
    devices = [InputDevice(dev) for dev in list_devices()]
    for device in devices:
        if "HID 16c0:27db" in device.name:
            return device
    return None

try:
    while True:
        device = find_rfid_event_device()

        if device is not None:
            print("RFID event device found:", device)
            break

        time.sleep(1)  # Wait for 1 second before rechecking

    print("Reading RFID data...")
    rfid_data = ""  # Initialize an empty string to store RFID data
    data_list = []
    
    for event in device.read_loop():
        # Process keyboard events here
        if event.type == ecodes.EV_KEY and event.value == 1:
            key_code = event.code
            if key_code in key_mapping:
                key = key_mapping[key_code]
                preview_data_len = len(data_list)
                
                if len(rfid_data) <= 10:
                    rfid_data += key  # Concatenate the keys into the RFID data string
                    if len(rfid_data) == 10:
                        data_list.append(rfid_data)
                        # print("RFID Data:", rfid_data)  # Print the RFID data string
                        rfid_data = ""
                    else:
                        pass
                else:
                    rfid_data = ""

                # update readed data list
                if len(data_list) != preview_data_len:
                    print("RFID Data:", data_list)
                
except KeyboardInterrupt:
    pass
finally:
    if device:
        device.close()
