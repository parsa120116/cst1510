with open("DATA/test.txt") as file:
    print("test.txt:")
    print(file.read())

with open("DATA/user_info.txt") as file:
    old_content = file.read()
print("user_info.txt (before):")
print(old_content)

new_line = "Course: CST1510 Programming for Data Communication and Networks"

with open("DATA/user_info.txt", "a") as file:
    if old_content != "" and not old_content.endswith("\n"):
        file.write("\n")          # the old text has no newline at the end, so add one first
    file.write(new_line + "\n")

with open("DATA/user_info.txt") as file:
    content = file.read()

lines = content.splitlines()
print()
print("user_info.txt (after):")
print(content)
print(f"Lines: {len(lines)}")
print(f"Characters: {len(content)}")
