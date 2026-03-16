import re

print("Terminal Command Risk Analyzer\n")

history_file = input("Enter path to bash history file: ")

danger_patterns = {
    "Delete Root Directory": r"rm\s+-rf\s+/\s*",
    "Recursive Delete": r"rm\s+-rf\s+",
    "Download and Execute": r"curl.*\|\s*sh",
    "Download Script": r"wget.*\.sh",
    "Permission Change": r"chmod\s+777",
    "Pipe to Bash": r"\|\s*bash",
    "Reverse Shell Indicator": r"nc\s+.*-e\s"
}

try:
    with open(history_file) as f:
        commands = [line.strip() for line in f if line.strip()]
except:
    print("Could not read history file")
    exit()

print("\nAnalyzing command history...\n")

alerts = 0

for cmd in commands:
    for name, pattern in danger_patterns.items():
        if re.search(pattern, cmd):
            print("[WARNING]", name)
            print("Command:", cmd)
            print()
            alerts += 1

print("Analysis complete\n")
print("Total commands analyzed:", len(commands))
print("Suspicious commands found:", alerts)
