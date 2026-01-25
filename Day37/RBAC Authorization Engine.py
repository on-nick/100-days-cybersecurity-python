# Roles and their permissions
roles = {
    "admin": {"read", "write", "delete", "audit"},
    "editor": {"read", "write"},
    "viewer": {"read"}
}

# Users mapped to roles
users = {
    "alice": "admin",
    "bob": "editor",
    "charlie": "viewer"
}

# Protected resources
resources = {
    "config": {"read", "write"},
    "logs": {"read", "audit"},
    "database": {"read", "write", "delete"}
}

def check_access(user, resource, action):
    if user not in users:
        return "DENY: Unknown user"

    role = users[user]
    role_perms = roles.get(role, set())
    resource_perms = resources.get(resource, set())

    if action in role_perms and action in resource_perms:
        return "ALLOW"
    return "DENY"

while True:
    print("\n1. Access Resource")
    print("2. Show Users")
    print("3. Exit")

    choice = input("Choice: ")

    if choice == "1":
        user = input("User: ")
        resource = input("Resource: ")
        action = input("Action: ")
        result = check_access(user, resource, action)
        print("Decision:", result)

    elif choice == "2":
        for u, r in users.items():
            print(u, "->", r)

    elif choice == "3":
        break
