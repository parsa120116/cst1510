name = "record check console"
print(name.title())    # first letter of every word in capitals
print(name.upper())    # every letter in capitals

original = "SRV-01"
print(original.lower())
print(original)
# original did not change because strings are immutable (they cannot be changed).
# .lower() does not change the old string; it RETURNS a NEW lowercase string.
# We printed that new string, but never stored it, so original is still "SRV-01".
