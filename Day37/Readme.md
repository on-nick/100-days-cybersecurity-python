### What I Learned
- How to implement **role-based access control (RBAC)** in Python.
- How to map users to roles and roles to permissions.
- How to check both **user permissions** and **resource restrictions** before allowing actions.
- How to structure a simple **CLI menu** for interacting with a program.

### What I Built
- A **user access management system** that decides whether a user can perform a specific action on a protected resource.
- A **command-line interface** to test access, list users, and exit the program.

### What Failed
- Initially, there could be **confusion if a user or resource didn’t exist** because we needed to handle unknown users and resources explicitly.
- At first, I didn’t combine **role permissions** with **resource permissions**, which caused incorrect “ALLOW” results.

### How I Fixed It
- Added a check for **unknown users**.
- Made sure an action is allowed only if it exists **in both the role’s permissions and the resource’s allowed actions**.

### Security Insight
- Even if a user has a role with a certain permission, they **cannot act on a resource that doesn’t allow that action**, which prevents accidental privilege escalation.
- Proper **RBAC checks** ensure only authorized users can read, write, delete, or audit sensitive resources.
