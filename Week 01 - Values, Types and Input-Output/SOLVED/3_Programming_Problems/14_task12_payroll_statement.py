name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: "))
hourly_rate = float(input("Enter hourly pay rate: "))
federal_rate = float(input("Enter federal tax rate (%): "))
state_rate = float(input("Enter state tax rate (%): "))

gross_pay = hours * hourly_rate
federal_withholding = gross_pay * federal_rate / 100
state_withholding = gross_pay * state_rate / 100
net_pay = gross_pay - federal_withholding - state_withholding

print(f"Employee: {name}")
print(f"Gross pay: £{gross_pay:.2f}")
print(f"Federal withholding: £{federal_withholding:.2f}")
print(f"State withholding: £{state_withholding:.2f}")
print(f"Net pay: £{net_pay:.2f}")
