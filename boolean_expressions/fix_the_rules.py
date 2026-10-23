#GharamAlkaraki
#fix_the_rules.py

# This program checks a connection against three rules.

role = input("Role: ")
port = int(input("Port: "))

# Semantic bug: use == to compare instead of = to assign.
is_admin = (role == "admin")

# Syntax bug: use <= instead of =<.
# Runtime bug: convert the input port to int before comparing.
is_system_port = (port <= 1023)

# Semantic bug: compare port with both values.
is_web_port = (port == 80 or port == 443)

print(f"Admin: {is_admin}")
print(f"System port: {is_system_port}")
print(f"Web port: {is_web_port}")