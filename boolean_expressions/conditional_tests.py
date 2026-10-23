#GharamAlkaraki
#conditional_tests.py 
user ="analyst"
role = "viewer"
failed = 3
port = 22

print("Is user == 'analyst'? I predict True.")
print(user == "analyst")

print("\nIs role == 'admin'? I predict False.")
print(role == "admin")

print("\nIs failed > 2? I predict True.")
print(failed > 2)

print("\nIs port == 443? I predict False.")
print(port == 443)

print("\nIs user != 'analyst'? I predict False.")
print(user != "analyst")

print("\nIs failed < 3? I predict False.")
print(failed < 3)

print("\nIs port <= 22? I predict True.")
print(port <= 22)

print("\nIs role == 'viewer' and port == 22? I predict True.")
print(role == "viewer" and port == 22)

print("\nIs user == 'admin' or failed < 3? I predict False.")
print(user == "admin" or failed < 3)

print("\nIs not (role == 'admin')? I predict True.")
print(not (role == "admin"))