import random


def add(number1, number2):
    """Return number1 + number2."""
    return number1 + number2


def subtract(number1, number2):
    """Return number1 - number2."""
    return number1 - number2


def multiply(number1, number2):
    """Return number1 * number2."""
    return number1 * number2


def divide(number1, number2):
    """Return number1 / number2 rounded to 2 d.p., or None when number2 is 0."""
    if number2 == 0:
        return None
    return round(number1 / number2, 2)


def exponent(number1, number2):
    """Return number1 to the power of number2."""
    return number1 ** number2


def remainder(number1, number2):
    """Return the remainder of number1 / number2, or None when number2 is 0."""
    if number2 == 0:
        return None
    return number1 % number2


def show_menu():
    """Print the operations the student can practise."""
    print()
    print("===== Maths Practice =====")
    print("1) Addition        (+)")
    print("2) Subtraction     (-)")
    print("3) Multiplication  (*)")
    print("4) Division        (/)")
    print("5) Exponent        (**)")
    print("6) Remainder       (%)")
    print("Q) Quit")


def is_number(text):
    """Return True if text is a number such as 7, -3 or 2.5."""
    if text.startswith("-"):
        text = text[1:]
    return text.replace(".", "", 1).isdigit()


def read_answer(question):
    """Ask the question until the user types a number; return it as a float."""
    while True:
        text = input(question).strip()
        if is_number(text):
            return float(text)
        print("Please type a number, for example 7 or 2.5")


def ask_question(choice):
    """Ask one random question; return "correct", "wrong" or "skipped"."""
    number1 = random.randint(0, 9)
    number2 = random.randint(0, 9)

    if choice == "1":
        symbol = "+"
        correct = add(number1, number2)
    elif choice == "2":
        symbol = "-"
        correct = subtract(number1, number2)
    elif choice == "3":
        symbol = "*"
        correct = multiply(number1, number2)
    elif choice == "4":
        symbol = "/"
        correct = divide(number1, number2)
    elif choice == "5":
        symbol = "**"
        correct = exponent(number1, number2)
    else:
        symbol = "%"
        correct = remainder(number1, number2)

    if correct is None:
        print(f"Error: {number1} {symbol} {number2} means dividing by zero, which is not allowed.")
        print("This question is skipped. Let's try another one!")
        return "skipped"

    if symbol == "/":
        print("(Give division answers to 2 decimal places.)")
    answer = read_answer(f"What is {number1} {symbol} {number2}? ")

    if round(answer, 2) == correct:
        print("Correct! Well done.")
        return "correct"
    print(f"Not quite. The answer is {correct}.")
    return "wrong"


def main():
    """Run the quiz until the student chooses to quit."""
    score = 0
    questions = 0
    while True:
        show_menu()
        choice = input("Choose an operation (1-6) or Q to quit: ").strip().upper()
        if choice == "Q":
            break
        if choice not in ("1", "2", "3", "4", "5", "6"):
            print("Sorry, that is not on the menu. Please choose 1-6 or Q.")
            continue

        result = ask_question(choice)
        if result == "skipped":
            continue
        questions += 1
        if result == "correct":
            score += 1
        print(f"Score: {score} / {questions}")

    print(f"Final score: {score} out of {questions}. Goodbye!")


if __name__ == "__main__":
    main()
