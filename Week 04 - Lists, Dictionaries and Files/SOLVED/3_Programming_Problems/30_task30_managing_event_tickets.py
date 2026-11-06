available_tickets = {"Concert": 100, "Football Game": 50, "Theater Show": 75, "Jazz Night": 1}
purchasers = {"Concert": ["John", "Emily"], "Football Game": ["Alex"],
              "Theater Show": ["Sam", "John"], "Jazz Night": []}
# "Jazz Night" is an extra event with only 1 ticket, to test "sold out"


def check_availability(tickets, event):
    """Print and return how many tickets are left for an event."""
    if event not in tickets:
        print(f"There is no event called '{event}'.")
        return 0
    print(f"{event}: {tickets[event]} tickets left")
    return tickets[event]


def buy_ticket(tickets, buyers, event, name):
    """Sell one ticket to name if possible. Return True if it worked."""
    if event not in tickets:
        print(f"Sorry {name}, there is no event called '{event}'.")
        return False
    if tickets[event] == 0:
        print(f"Sorry {name}, {event} is sold out.")
        return False
    tickets[event] -= 1
    buyers[event].append(name)
    print(f"{name} bought a ticket for {event}. Tickets left: {tickets[event]}")
    return True


def view_purchasers(buyers, event):
    """Print everyone who bought a ticket for an event."""
    if event not in buyers or len(buyers[event]) == 0:
        print(f"No one has bought tickets for {event} yet.")
    else:
        print(f"{event} buyers: {', '.join(buyers[event])}")


check_availability(available_tickets, "Concert")
buy_ticket(available_tickets, purchasers, "Concert", "Sara")
buy_ticket(available_tickets, purchasers, "Jazz Night", "Parsa")
buy_ticket(available_tickets, purchasers, "Jazz Night", "Emily")
buy_ticket(available_tickets, purchasers, "Opera", "Alex")
print()
view_purchasers(purchasers, "Concert")
view_purchasers(purchasers, "Jazz Night")
print()
print("--- All events ---")
for event in available_tickets:
    sold = len(purchasers[event])
    print(f"{event:<14} left: {available_tickets[event]:>3}   sold: {sold}")
