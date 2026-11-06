with open("DATA/python_zen.txt") as file:
    lines = file.readlines()

title = lines[0]
number = 1

with open("numbered_zen.txt", "w") as out_file:
    out_file.write(title)                     # the title keeps no number
    for line in lines[1:]:
        text = line.rstrip("\n")
        if text == "":
            out_file.write("\n")              # keep the empty line, but don't number it
        else:
            out_file.write(f"{number}. {text}\n")
            number += 1

# Show the result
with open("numbered_zen.txt") as check_file:
    print(check_file.read())
