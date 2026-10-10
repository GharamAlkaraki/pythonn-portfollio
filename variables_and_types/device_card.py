# device_card.py
# This program stores network device information in variables and prints them.

MAX_CONNECTIONS = 90


device_name,device_ip,service,open_port = "web-server-01","170.0.2.12","HTTPS", 400

print("Device:", device_name)
print("IP address:", device_ip)
print("Service:", service)
print("Port:", open_port)
print("Max connections:", MAX_CONNECTIONS)

open_port,service = 22,"HTTP"

print("Updated service:", service, "on port:", open_port)