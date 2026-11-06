import random

ticket = []
while len(ticket) < 6:
    number = random.randint(1, 49)
    if number not in ticket:
        ticket.append(number)

ticket.sort()
print("Your lottery numbers:", " ".join([str(number) for number in ticket]))
