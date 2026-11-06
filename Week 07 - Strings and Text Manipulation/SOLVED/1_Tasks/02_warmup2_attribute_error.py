# FIXED: clean the TEXT first (strip is a string method), then convert to a number.

value_text = "87"
cleaned = value_text.strip()

value = float(cleaned)
print(value)
