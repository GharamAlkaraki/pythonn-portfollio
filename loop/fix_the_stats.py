#GharamAlkaraki
# fix_the_stats.py
# Count failed logins & the average session length.
events = ["FAILED", "SUCCESS", "FAILED", "SUCCESS", "SUCCESS"]
minutes = [8, 30, 0, 15, 45]

# BUG 1 FIX: failed was reset to 0 inside loop  moved outside so it counts correctly
failed = 0
for event in events:
    if event == "FAILED":
        failed += 1
print(f"Failed logins: {failed}")

total = 0
count = 0
for value in minutes:
    if value > 0:
        total += value
        count += 1

# BUG 2 FIX: print was inside loop causing repeated output, moved outside
# BUG 3 FIX: used // which gives int, need / to get 30.0
print(f"Average session: {total / count} minutes")

# BUG 4 FIX: range(1,4) stops at 3, need range(1,5) to include 4
for level in range(1, 5):
    print(f"Level {level}")