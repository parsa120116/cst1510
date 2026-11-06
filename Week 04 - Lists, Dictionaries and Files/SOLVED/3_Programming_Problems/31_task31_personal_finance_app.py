expenses = {"Food": [25, 40, 15], "Entertainment": [50, 20], "Travel": [300, 150]}


def read_amount(prompt):
    """Keep asking until the user types a valid positive number."""
    while True:
        text = input(prompt)
        try:
            amount = float(text)
            if amount > 0:
                return amount
            print("The amount must be more than 0.")
        except ValueError:
            print(f"'{text}' is not a number. Try again.")


def add_expense(expenses, category, amount):
    """Add one expense to a category (creates the category if needed)."""
    if category not in expenses:
        expenses[category] = []
    expenses[category].append(amount)
    print(f"Added £{amount:.2f} to {category}.")


def remove_expense(expenses, category, amount):
    """Remove one expense of this amount from a category, if it exists."""
    if category in expenses and amount in expenses[category]:
        expenses[category].remove(amount)
        print(f"Removed £{amount:.2f} from {category}.")
        if len(expenses[category]) == 0:
            del expenses[category]          # no expenses left in this category
    else:
        print(f"No expense of £{amount:.2f} found in {category}.")


def show_summary(expenses):
    """Print the total spent in each category and the grand total."""
    print("----- Spending summary -----")
    grand_total = 0
    for category, amounts in expenses.items():
        total = sum(amounts)
        grand_total += total
        print(f"{category:<15} £{total:>8.2f}  ({len(amounts)} items)")
    print(f"{'TOTAL':<15} £{grand_total:>8.2f}")
    print("----------------------------")


while True:
    print("\n1) Add expense  2) Remove expense  3) Summary  4) Quit")
    choice = input("Choose 1-4: ").strip()
    if choice == "1":
        category = input("Category: ").strip().title()
        amount = read_amount("Amount: £")
        add_expense(expenses, category, amount)
    elif choice == "2":
        category = input("Category: ").strip().title()
        amount = read_amount("Amount to remove: £")
        remove_expense(expenses, category, amount)
    elif choice == "3":
        show_summary(expenses)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Please choose 1, 2, 3 or 4.")
