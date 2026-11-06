value = 87
limit = 100

percent = (value / limit) * 100

if percent >= 100:
    print("OVER LIMIT")
elif percent >= 90:
    print("WARNING")
else:
    print("OK")
