from scapy.all import ARP, sniff

print("ARP Spoofing Detector\n")

ip_mac_table = {}

def process_packet(packet):
    if packet.haslayer(ARP) and packet[ARP].op == 2:  # ARP reply
        ip = packet[ARP].psrc
        mac = packet[ARP].hwsrc

        if ip in ip_mac_table:
            if ip_mac_table[ip] != mac:
                print("[ALERT] Possible ARP Spoofing Detected!")
                print("IP Address:", ip)
                print("Original MAC:", ip_mac_table[ip])
                print("New MAC:", mac)
                print()
        else:
            ip_mac_table[ip] = mac

print("Monitoring network...\n")

sniff(filter="arp", store=False, prn=process_packet)
