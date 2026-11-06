ip_address = input("IP address: ")
method = input("HTTP method: ")
path = input("Path: ")
status = int(input("Status code: "))
size_bytes = int(input("Bytes sent: "))

print(f'{ip_address} - "{method} {path}" {status} {size_bytes}')
