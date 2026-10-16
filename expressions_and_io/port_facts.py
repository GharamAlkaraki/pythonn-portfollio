#GharamAlkaraki
#port_facts.py
# Description: Port and IPv4 Address Calculations based on RFC standards.
# References:
# RFC 9293 - TCP 
# RFC 791  - Internet Protocol (IPv4) 
PORT_BITS = 16
IPV4_BITS = 32
total_ports = 2 ** PORT_BITS
highest_port = (2 ** PORT_BITS) - 1
total_ipv4_addresses = 2 ** IPV4_BITS
print(f"Total possible TCP ports: {total_ports}")
print(f"Highest TCP port number: {highest_port}")
print(f"Total possible IPv4 addresses: {total_ipv4_addresses}")