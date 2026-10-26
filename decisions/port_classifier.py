#GharamAlkaraki
# port_classifier.py
port = int(input("Port: "))

if port < 0 or port > 65535:
    print("Invalid port: use a number from 0 to 65535.")
else:
  
    if port <= 1023:
       range_str = "system"
    elif port <= 49151:
        range_str = "user"
    else:
        range_str = "dynamic or private"
    
    print(f"Range: {range_str}")
    
    if port == 22:
        print("Service: ssh")
    elif port == 80:
        print("Service: http")
    elif port == 443:
        print("Service: https")