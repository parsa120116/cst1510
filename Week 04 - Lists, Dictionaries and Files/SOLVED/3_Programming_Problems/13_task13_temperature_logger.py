temperatures = []
for day in range(1, 6):
    temperature = float(input(f"Enter the temperature for day {day} (°C): "))
    temperatures.append(temperature)

# 2. Write each temperature with its day number, e.g. "Day 1: 22°C"
with open("temps.txt", "w") as file:
    for day in range(1, 6):
        file.write(f"Day {day}: {temperatures[day - 1]:g}°C\n")

# 3. Read the file back and work out the average
total = 0
count = 0
with open("temps.txt", "r") as file:
    for line in file:
        line = line.strip()
        print(line)
        number_text = line.split(": ")[1].split("°C")[0]
        total += float(number_text)
        count += 1

average = total / count
print(f"Average temperature: {average:.1f}°C")
