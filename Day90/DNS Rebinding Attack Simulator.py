import http.server
import socketserver
import threading
import time

PORT = 8000

# Simple web server to simulate internal service
class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Internal Service Accessed")

def start_server():
    with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
        print(f"[+] Internal server running on port {PORT}")
        httpd.serve_forever()

# Simulate DNS rebinding behavior
def simulate_dns_rebinding():
    print("[*] Simulating DNS Rebinding Attack...\n")

    fake_dns = {
        "malicious.com": ["1.2.3.4", "127.0.0.1"]
    }

    for domain, ips in fake_dns.items():
        print(f"[+] Resolving {domain} -> {ips[0]} (External IP)")
        time.sleep(2)
        print(f"[+] Rebinding {domain} -> {ips[1]} (Internal IP)")
        print("[!] Browser now accesses internal service via same domain\n")

if __name__ == "__main__":
    t = threading.Thread(target=start_server, daemon=True)
    t.start()

    time.sleep(1)
    simulate_dns_rebinding()

    while True:
        time.sleep(10)
