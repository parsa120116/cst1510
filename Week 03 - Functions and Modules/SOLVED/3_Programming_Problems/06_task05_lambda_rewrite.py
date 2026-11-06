import random

# Each maths operation is now a one-line lambda, stored in a dictionary
# under its symbol. Division and remainder give None when b is 0.
OPERATIONS = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: round(a / b, 2) if b != 0 else None,
    "**": lambda a, b: a ** b,
    "%": lambda a, b: a % b if b != 0 else None,
}

# Small helpers written as lambdas too
random_digit = lambda: random.randint(0, 9)
is_number = lambda text: (text[1:] if text.startswith("-") else text).replace(".", "", 1).isdigit()
is_correct = lambda answer, correct: round(answer, 2) == correct


def main():
    """Run the lambda version of the quiz until the user types q."""
    score = 0
    questions = 0
    while True:
        print()
        print("Operations:  +   -   *   /   **   %")
        symbol = input("Type the operation to practise (or q to quit): ").strip().lower()
        if symbol == "q":
            break
        if symbol not in OPERATIONS:
            print("Sorry, that operation is not on the list.")
            continue

        number1 = random_digit()
        number2 = random_digit()
        correct = OPERATIONS[symbol](number1, number2)
        if correct is None:
            print(f"Error: {number1} {symbol} {number2} divides by zero. Let's skip this one.")
            continue

        if symbol == "/":
            print("(Give division answers to 2 decimal places.)")
        text = input(f"What is {number1} {symbol} {number2}? ").strip()
        while not is_number(text):
            text = input("Please type a number: ").strip()

        questions += 1
        if is_correct(float(text), correct):
            score += 1
            print("Correct! Well done.")
        else:
            print(f"Not quite. The answer is {correct}.")
        print(f"Score: {score} / {questions}")

    print(f"Final score: {score} out of {questions}. Goodbye!")


if __name__ == "__main__":
    main()
