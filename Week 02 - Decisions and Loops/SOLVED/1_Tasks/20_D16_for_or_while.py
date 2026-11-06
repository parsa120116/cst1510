# a) for: I know in advance it runs exactly 3 times.
for i in range(3):
    number = float(input("Enter a number: "))
    print("You typed", number)

# b) while: I don't know how many tries the user will need.
password = input("Password: ")
while password != "letmein":
    password = input("Wrong. Password: ")
print("Welcome")
