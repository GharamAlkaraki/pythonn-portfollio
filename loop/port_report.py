#GharamAlkaraki 
#port_report.py


start = int(input("Start port: "))
end = int(input("End port: "))
count = 0
for port in range(start, end + 1):
    count += 1
    if port <= 1023:
        kind = "system"
    elif port <= 49151:
        kind = "user"
    else:
        kind = "dynamic"
    print(f"{port}: {kind}")
print(f"Ports checked: {count}")