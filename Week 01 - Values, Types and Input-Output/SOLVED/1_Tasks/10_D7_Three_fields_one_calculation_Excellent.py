label = input("Label: ")
part = float(input("Part: "))
total = float(input("Total: "))

percent = part / total * 100

print(f"{label:<15}: {part:>3.0f} of {total:.0f}  =  {percent:.1f} %")
