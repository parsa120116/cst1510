filename = input("Enter a file name: ")

try:
    with open(filename) as file:
        print(file.read())
except FileNotFoundError:
    print("File not found")
except Exception as error:
    print(f"Sorry, something went wrong: {error}")
