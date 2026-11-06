responses = [
    "  VERY SATISFIED  ",
    "somewhat happy   ",
    "  NOT Happy  ",
    "   NEUTRAL",
    "  dissatisfied  "
]

cleaned_responses = []
for response in responses:
    cleaned = response.strip().lower()
    cleaned_responses.append(cleaned)
    print(f"[{response}] -> [{cleaned}]")

print()
print("Cleaned list:", cleaned_responses)
