#Gharam Alkaraki
#fix_the_session.py
# Description: Fixed session timer code with bug explanations.

username = input("Username: ")

# Fix 1 (runtime error): input() returns string, converted to int for calculations
total_seconds = int(input("Session length in seconds: "))

# Fix 2 (semantic error): used integer division // instead of float division /
minutes = total_seconds // 60
seconds = total_seconds % 60

print("=" * 30)

# Fix 3 (runtime error): fixed syntax/string formatting using f-string
print(f"User: {username}")

# Fix 4 (semantic error): fixed output structure to match goal requirements
print(f"Session: {minutes} min {seconds} s")

print("=" * 30)