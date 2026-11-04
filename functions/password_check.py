#GharamAlkaraki
#password_check.py  
def long_enough(password, minimum=8):
    """True if password length >= minimum."""
    return len(password) >= minimum

def differs_from_username(password, username):
    """True if password and username are not equal."""
    return password != username

def password_ok(password, username):
    """True only if both checks pass."""
    return long_enough(password) and differs_from_username(password, username)

username = input("Username: ")
password = input("Password: ")

if password_ok(password, username):
    print("Password accepted.")
else:
    print("Password rejected.")