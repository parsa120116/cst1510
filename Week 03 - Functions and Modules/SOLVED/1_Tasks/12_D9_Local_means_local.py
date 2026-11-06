# Prediction: "inside: OK" is printed, then a NameError for result.
def make_status():
    result = "OK"
    print("inside:", result)

make_status()
print("outside:", result)
# result was created inside make_status, so it only exists while the
# function runs. Outside the function the name does not exist -> NameError.
