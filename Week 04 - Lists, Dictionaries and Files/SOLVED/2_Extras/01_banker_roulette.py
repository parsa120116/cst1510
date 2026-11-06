import random

friends = ["Alice", "Bob", "Charlie", "Diana", "Emma"]

# Way 1: let random pick an item directly
print(random.choice(friends))

# Way 2: pick a random index, then use it
index = random.randint(0, len(friends) - 1)
print(friends[index])
