# Prediction: 42, then 21.
def double(n):
    n = n * 2
    return n

number = 21
print(double(number))
print(number)
# number is still 21: the function received a COPY of the value (21) in its
# own local name n. Changing n inside does not change number outside.
