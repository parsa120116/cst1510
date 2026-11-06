MENU = {
    "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
    "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0},
}

resources = {"water": 300, "milk": 200, "coffee": 100}
money = 0.0


def report(resources, money):
    """Print the machine's resources and money."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money:.2f}")


def missing_ingredients(ingredients, resources):
    """Return a list of the ingredients there is not enough of."""
    missing = []
    for item, amount in ingredients.items():
        if resources.get(item, 0) < amount:
            missing.append(item)
    return missing


def make_coffee(drink_name, ingredients, resources):
    """Take the drink's ingredients out of the resources."""
    for item, amount in ingredients.items():
        resources[item] -= amount
    print(f"Here is your {drink_name} ☕️. Enjoy!")


machine_on = True
while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        machine_on = False
    elif choice == "report":
        report(resources, money)
    elif choice in MENU:
        drink = MENU[choice]
        missing = missing_ingredients(drink["ingredients"], resources)
        if missing:
            print(f"Sorry, there is not enough {', '.join(missing)}.")
        else:
            paid = float(input(f"That's ${drink['cost']:.2f}. How much do you insert? $"))
            if paid < drink["cost"]:
                print("Sorry, that's not enough money. Money refunded.")
            else:
                change = paid - drink["cost"]
                money += drink["cost"]
                if change > 0:
                    print(f"Here is ${change:.2f} in change.")
                make_coffee(choice, drink["ingredients"], resources)
    else:
        print("Sorry, we don't have that.")
