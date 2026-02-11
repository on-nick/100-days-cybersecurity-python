import os

SYSTEM_PROCESS_NAMES = {
    "systemd", "kthreadd", "kworker", "sshd",
    "cron", "dbus-daemon", "NetworkManager"
}

SUSPICIOUS_LOCATIONS = ["/tmp", "/dev/shm", "/var/tmp"]

print("Process Masquerading Detector Started\n")

for pid in os.listdir("/proc"):
    if not pid.isdigit():
        continue

    try:
        with open(f"/proc/{pid}/comm", "r") as f:
            name = f.read().strip()

        exe_path = os.readlink(f"/proc/{pid}/exe")

        # Case 1: System process name running from suspicious directory
        if name in SYSTEM_PROCESS_NAMES:
            for loc in SUSPICIOUS_LOCATIONS:
                if exe_path.startswith(loc):
                    print(f"[ALERT] Masquerading detected:")
                    print(f" PID: {pid}")
                    print(f" Name: {name}")
                    print(f" Executable: {exe_path}\n")

        # Case 2: Executable deleted but still running
        if "(deleted)" in exe_path:
            print(f"[ALERT] Running deleted executable:")
            print(f" PID: {pid}")
            print(f" Name: {name}")
            print(f" Path: {exe_path}\n")

    except:
        continue
