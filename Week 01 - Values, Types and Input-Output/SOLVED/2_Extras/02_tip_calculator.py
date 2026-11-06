print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill? "))
tip_percent = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

total_with_tip = bill * (1 + tip_percent / 100)
each_pays = total_with_tip / people

print(f"Each person should pay: ${each_pays:.2f}")
