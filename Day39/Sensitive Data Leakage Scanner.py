import os
import re

PATTERNS = {
    "Email": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "Credit Card": r"\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b",
    "Google API Key": r"AIza[0-9A-Za-z\-_]{35}",
    "AWS Access Key": r"AKIA[0-9A-Z]{16}",
    "JWT Token": r"eyJ[A-Za-z0-9_-]+\.eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+",
    "Private Key": r"-----BEGIN PRIVATE KEY-----",
    "Password": r"(?i)(password|passwd|pwd)\s*=\s*['\"].+?['\"]",
    "Token": r"(?i)(token|secret|apikey|api_key)\s*=\s*['\"].+?['\"]"
}

EXTENSIONS = (
    ".txt", ".log", ".env", ".py", ".js", ".php", ".json",
    ".yaml", ".yml", ".conf", ".bak", ".old", ".ini"
)

def mask_data(text):
    if len(text) <= 6:
        return text
    return text[:3] + "*" * (len(text) - 6) + text[-3:]

def scan_file(file_path):
    results = []
    try:
        with open(file_path, "r", errors="ignore") as f:
            lines = f.readlines()
    except:
        return results

    for i, line in enumerate(lines, start=1):
        for name, pattern in PATTERNS.items():
            matches = re.findall(pattern, line)
            for m in matches:
                if isinstance(m, tuple):
                    m = m[0]
                masked = mask_data(str(m))
                results.append((name, file_path, i, masked))
    return results

def scan_folder(folder):
    all_results = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            path = os.path.join(root, file)
            if path.endswith(EXTENSIONS):
                res = scan_file(path)
                all_results.extend(res)
    return all_results

def main():
    folder = input("Enter directory to scan: ").strip()

    if not os.path.exists(folder):
        print("Directory not found")
        return

    print("\n========== Sensitive Data Leakage Scan ==========\n")

    results = scan_folder(folder)

    if not results:
        print("No sensitive data found.")
    else:
        for name, file_path, line_no, value in results:
            print("[ALERT]")
            print("Type :", name)
            print("File :", file_path)
            print("Line :", line_no)
            print("Data :", value)
            print("-" * 50)

    print("\nScan completed.")

if __name__ == "__main__":
    main()
