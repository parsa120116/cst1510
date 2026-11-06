import random

number1 = random.randint(0, 9)
number2 = random.randint(0, 9)
correct_answer = number1 * number2

answer = int(input(f"What is {number1} * {number2}? "))

if answer == correct_answer:
    print(f"{number1} * {number2} = {answer} is true")
else:
    print(f"{number1} * {number2} = {answer} is false")
    print(f"The correct answer is {correct_answer}")
