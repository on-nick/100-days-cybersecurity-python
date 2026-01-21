rules = []

def add_rule():
    ip = input("Enter IP: ")
    port = input("Enter Port: ")
    action = input("Action (allow/deny): ")
    rules.append({"ip": ip, "port": port, "action": action})
    print("Rule added")

def check_packet():
    ip = input("Source IP: ")
    port = input("Destination Port: ")

    for rule in rules:
        if rule["ip"] == ip and rule["port"] == port:
            print("Packet", rule["action"].upper())
            return
    print("Packet ALLOWED (no matching rule)")

while True:
    print("\n1. Add Firewall Rule")
    print("2. Check Network Packet")
    print("3. Show Rules")
    print("4. Exit")

    choice = input("Choice: ")

    if choice == "1":
        add_rule()
    elif choice == "2":
        check_packet()
    elif choice == "3":
        for r in rules:
            print(r)
    elif choice == "4":
        break
    else:
        print("Invalid option")
