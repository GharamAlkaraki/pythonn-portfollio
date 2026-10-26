# risk_score.py
#GharamAlkaraki
score = 0

failed_attempts = int(input("Failed attempts in the last hour: "))
login_hour = int(input("Login hour (0-23): "))
new_device = input("New device (yes/no): ")

if failed_attempts >= 3:
    score += 40

if login_hour < 6:
    score += 30

if new_device == "yes":
    score += 30

if score >= 70:
    level = "HIGH"
elif score >= 30:
    level = "MEDIUM"
else:
    level = "LOW"

print(f"Risk score: {score} ({level})")