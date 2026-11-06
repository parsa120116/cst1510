values = [10, 20, 30]

values[0] = 99          # replace the item at position 0
print(values)

values.append(40)       # add to the end
print(values)

values.remove(20)       # remove the first item equal to 20
print(values)

for value in values:    # visit each item in turn
    print(value)
