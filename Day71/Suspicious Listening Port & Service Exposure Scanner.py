import os
import socket

PROC_TCP = "/proc/net/tcp"
PROC_UDP = "/proc/net/udp"

COMMON_PORTS = {22, 80, 443}
HIGH_RISK_PORTS = {21, 23, 25, 3389, 5900}

def hex_to_ip(hex_ip):
    return socket.inet_ntoa(bytes.fromhex(hex_ip)[::-1])

def hex_to_port(hex_port):
    return int(hex_port, 16)

def scan_protocol(file_path, proto_name):
    if not os.path.isfile(file_path):
        return

    with open(file_path, "r") as f:
        lines = f.readlines()[1:]

    for line in lines:
        parts = line.split()
        local_address = parts[1]
        state = parts[3]

        # 0A = LISTEN state for TCP
        if proto_name == "TCP" and state != "0A":
            continue

        ip_hex, port_hex = local_address.split(":")
        ip = hex_to_ip(ip_hex)
        port = hex_to_port(port_hex)

        if port not in COMMON_PORTS:
            print(f"[INFO] {proto_name} Service Listening on {ip}:{port}")

            if port in HIGH_RISK_PORTS:
                print("  [ALERT] High-risk service exposed\n")

print("Service Exposure Scanner Started\n")

scan_protocol(PROC_TCP, "TCP")
scan_protocol(PROC_UDP, "UDP")

print("Scan Complete")
