def within_limit(value, limit):
    return value <= limit

print(within_limit(87, 100))
print(within_limit(100, 87))
# Different because arguments are matched by POSITION:
# first call: value=87, limit=100 -> 87 <= 100 -> True
# second call: value=100, limit=87 -> 100 <= 87 -> False
