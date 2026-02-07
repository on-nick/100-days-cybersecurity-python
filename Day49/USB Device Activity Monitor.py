import os
import time

USB_PATH = "/dev"
SCAN_INTERVAL = 2

def get_devices():
    return set(os.listdir(USB_PATH))

print("USB Device Monitor Started...\n")

previous_devices = get_devices()

while True:
    time.sleep(SCAN_INTERVAL)
    current_devices = get_devices()

    added = current_devices - previous_devices
    removed = previous_devices - current_devices

    for d in added:
        if d.startswith("sd"):
            print(f"[ALERT] USB device connected: {d}")

    for d in removed:
        if d.startswith("sd"):
            print(f"[ALERT] USB device removed: {d}")

    previous_devices = current_devices
