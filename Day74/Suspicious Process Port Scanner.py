import os
import socket

print("Suspicious Process Port Scanner\n")

connections = {}

# Read TCP connections
with open("/proc/net/tcp", "r") as f:
    lines = f.readlines()[1:]

for line in lines:
    parts = line.split()
    local_address = parts[1]
    inode = parts[9]

    ip_hex, port_hex = local_address.split(":")
    port = int(port_hex, 16)

    connections[inode] = port


# Match inode with running processes
for pid in os.listdir("/proc"):
    if pid.isdigit():
        fd_path = f"/proc/{pid}/fd"

        try:
            for fd in os.listdir(fd_path):
                link = os.readlink(f"{fd_path}/{fd}")

                if "socket:[" in link:
                    inode = link.split("[")[1].strip("]")

                    if inode in connections:
                        port = connections[inode]
                        if port > 1024:
                            print(f"Process {pid} is listening on suspicious port {port}")

        except:
            continue
