def add(n1, n2):
    """Return n1 + n2."""
    return n1 + n2

def subtract(n1, n2):
    """Return n1 - n2."""
    return n1 - n2

def multiply(n1, n2):
    """Return n1 * n2."""
    return n1 * n2

def divide(n1, n2):
    """Return n1 / n2."""
    return n1 / n2

operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

n1 = float(input("What's the first number? "))
keep_going = True

while keep_going:
    operator = input("Pick an operation (+ - * /): ")
    if operator not in operations:
        print("Unknown operation, try again.")
        continue
    n2 = float(input("What's the next number? "))

    result = operations[operator](n1, n2)
    print(f"{n1} {operator} {n2} = {result}")

    choice = input("Type 'y' to continue with the result, 'n' to start over, or 'q' to quit: ")
    if choice == "y":
        n1 = result
    elif choice == "n":
        n1 = float(input("What's the first number? "))
    else:
        keep_going = False

print("Goodbye!")
