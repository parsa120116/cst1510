human_years = float(input("Enter the number of human years: "))

if human_years < 0:
    print("Error: the number of years cannot be negative.")
elif human_years <= 2:
    dog_years = human_years * 10.5
    print(f"{human_years} human years is {dog_years} dog years.")
else:
    dog_years = 2 * 10.5 + (human_years - 2) * 4
    print(f"{human_years} human years is {dog_years} dog years.")
