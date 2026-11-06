hostnames = ["srv-01", "srv-02", "srv-03"]
used = [87, 45, 120]

usage = dict(zip(hostnames, used))
print(usage)
print(usage["srv-03"])
