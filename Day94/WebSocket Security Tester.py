import socket

print("WebSocket Security Tester\n")

host = input("Enter target host (example.com): ")
port = int(input("Enter port (usually 80 or 443): "))
path = input("Enter WebSocket path (example: /ws): ")

# Craft WebSocket handshake with malicious Origin
request = (
    f"GET {path} HTTP/1.1\r\n"
    f"Host: {host}\r\n"
    "Upgrade: websocket\r\n"
    "Connection: Upgrade\r\n"
    "Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==\r\n"
    "Sec-WebSocket-Version: 13\r\n"
    "Origin: https://evil.com\r\n"
    "\r\n"
)

print("\n[*] Sending WebSocket handshake...\n")

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send(request.encode())

    response = s.recv(4096).decode(errors="ignore")
    s.close()

    print("[*] Server Response:\n")
    print(response[:500])

    print("\nAnalysis:\n")

    if "101 Switching Protocols" in response:
        if "Sec-WebSocket-Accept" in response:
            print("[WARNING] WebSocket connection accepted with malicious Origin")
            print("Possible missing Origin validation")
        else:
            print("[INFO] Upgrade attempted but response incomplete")
    else:
        print("[INFO] WebSocket upgrade rejected")

except:
    print("Connection failed")
