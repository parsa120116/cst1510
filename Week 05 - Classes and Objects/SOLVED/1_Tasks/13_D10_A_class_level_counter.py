class Counted:
    count = 0                    # class attribute: ONE value shared by the class

    def __init__(self):
        Counted.count += 1       # change the shared value through the class name

a = Counted()
b = Counted()
c = Counted()
print(Counted.count)
# The count is shared because it belongs to the CLASS, not to each object.
# There is only one Counted.count; every new object adds 1 to that same number.
