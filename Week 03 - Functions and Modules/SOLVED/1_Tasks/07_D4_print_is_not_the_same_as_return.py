# Prediction: it prints 87.0 (from inside the function), then None.
def show_percent(part, total):
    print((part / total) * 100)

result = show_percent(87, 100)
print(result)
# The second line is None because show_percent has no return statement.
# A function without return gives back None ("nothing"),
# so result stores None even though 87.0 was shown on the screen.
