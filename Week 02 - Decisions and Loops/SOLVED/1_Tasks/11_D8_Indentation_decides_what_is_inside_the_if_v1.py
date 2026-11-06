# Prediction: 50 > 100 is False, so "OVER LIMIT" is skipped,
# but "Check finished" is NOT indented, so it always runs.
value = 50
limit = 100

if value > limit:
    print("OVER LIMIT")
print("Check finished")
