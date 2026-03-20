import time
import statistics

print("Keystroke Dynamics Analyzer\n")

SAMPLE_TEXT = "securelogin"

def capture_timings():
    print(f"\nType this text exactly: {SAMPLE_TEXT}")
    timings = []

    input("Press Enter when ready...")

    last_time = time.time()

    typed = ""
    while len(typed) < len(SAMPLE_TEXT):
        char = input()[0]  # take first char of input
        current_time = time.time()

        timings.append(current_time - last_time)
        last_time = current_time

        typed += char

    return timings


def compare_patterns(base, new):
    diffs = [abs(b - n) for b, n in zip(base, new)]
    return sum(diffs) / len(diffs)


print("Step 1: Create typing profile")
baseline = capture_timings()

print("\nStep 2: Verify user")
attempt = capture_timings()

score = compare_patterns(baseline, attempt)

print("\nAnalysis:\n")

print("Baseline timings:", [round(x, 3) for x in baseline])
print("Attempt timings:", [round(x, 3) for x in attempt])
print("Difference score:", round(score, 3))

if score < 0.2:
    print("\n[AUTH SUCCESS] Typing pattern matches user")
else:
    print("\n[AUTH FAILED] Typing pattern does not match")
