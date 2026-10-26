# fix_the_policy.py
#GharamAlkaraki
# Check a new password against an example policy and classify its length.
MIN_LENGTH = 12

username = input("Username: ")
password = input("New password: ")
#Syntax Error
if len(password) < MIN_LENGTH:
    print("- Too short.")
elif password == username:
    print("- Same as the username.")
#Semantic Error
if len(password) >= MIN_LENGTH:
    if len(password) >= 16:
        strength = "long"
    else:
        strength = "short"  
        
    print(f"Length: {len(password)} ({strength})")