import os
import stat

GTFO_SUSPECTS = {
    "find", "vim", "nano", "less", "more",
    "cp", "mv", "awk", "perl", "python",
    "ruby", "bash", "sh", "tar"
}

SEARCH_PATHS = ["/bin", "/usr/bin", "/usr/local/bin"]

print("GTFOBins SUID Abuse Detector Started\n")

for base in SEARCH_PATHS:
    if not os.path.isdir(base):
        continue

    for root, _, files in os.walk(base):
        for file in files:
            path = os.path.join(root, file)

            try:
                st = os.stat(path)
                if st.st_mode & stat.S_ISUID:
                    if file in GTFO_SUSPECTS:
                        print("[CRITICAL] High-risk SUID binary found:")
                        print(" Path:", path)
                        print(" Binary:", file, "\n")
                    else:
                        print("[INFO] SUID binary:", path)

            except:
                continue

print("Scan Complete")
