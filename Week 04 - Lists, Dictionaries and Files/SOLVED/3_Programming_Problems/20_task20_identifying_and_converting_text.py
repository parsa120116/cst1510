with open("DATA/Les_Brown.txt") as file:
    text = file.read()

chosen_part = "It's not over until I win!"

if chosen_part in text:
    new_text = text.replace(chosen_part, chosen_part.upper())
    with open("posiability.txt", "w") as out_file:
        out_file.write(new_text)
    print("Saved posiability.txt. The changed line is now:")
    print(chosen_part.upper())
else:
    print("That part was not found in the file. Check the spelling.")
