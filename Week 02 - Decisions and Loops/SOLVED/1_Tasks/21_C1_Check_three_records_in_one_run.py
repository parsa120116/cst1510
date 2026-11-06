for record_number in range(1, 4):
    print(f"Record {record_number}")
    value = float(input("Value: "))
    limit = float(input("Limit: "))

    if value > limit:
        print("OVER LIMIT")
    else:
        print("OK")
