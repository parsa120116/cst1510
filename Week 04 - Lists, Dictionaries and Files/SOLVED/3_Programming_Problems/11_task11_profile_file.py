name = "Alex"
age = 20
favorite_color = "Blue"

# 1 and 2: create the file and write three lines
with open("my_profile.txt", "w") as file:
    file.write(name + "\n")
    file.write(str(age) + "\n")
    file.write(favorite_color + "\n")

# 3: read the file back and print each line with a label
labels = ["Name", "Age", "Favorite Color"]

with open("my_profile.txt", "r") as file:
    lines = file.readlines()

for index in range(len(lines)):
    print(f"{labels[index]}: {lines[index].strip()}")
