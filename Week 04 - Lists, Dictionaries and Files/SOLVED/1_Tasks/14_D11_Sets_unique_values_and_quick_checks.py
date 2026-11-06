ips = ["10.0.0.5", "10.0.0.9", "10.0.0.5", "10.0.0.7"]

unique_ips = set(ips)
print(len(unique_ips))
print("10.0.0.9" in unique_ips)
print("10.0.0.1" in unique_ips)
