import os
import stat

SCAN_PATHS = ["/bin", "/usr/bin", "/usr/local/bin", "/sbin", "/usr/sbin"]
KNOWN_SYSTEM_BINARIES = {
    "passwd", "sudo", "su", "mount", "umount",
    "ping", "chsh", "chfn", "newgrp"
}

print("Hidden SetUID / SetGID Scanner Started\n")

for base in SCAN_PATHS:
    if not os.path.isdir(base):
        continue

    for root, _, files in os.walk(base):
        for file in files:
            path = os.path.join(root, file)

            try:
                st = os.stat(path)
                mode = st.st_mode

                is_setuid = bool(mode & stat.S_ISUID)
                is_setgid = bool(mode & stat.S_ISGID)

                if is_setuid or is_setgid:
                    if file not in KNOWN_SYSTEM_BINARIES:
                        print("[ALERT] Suspicious privileged binary found:")
                        print(" Path:", path)
                        print(" SetUID:", is_setuid, "| SetGID:", is_setgid, "\n")

            except:
                continue

print("Scan Complete")
