feedback = [
    "The product quality is great",
    "Fast delivery but poor quality",
    "Great product and great delivery",
    "Quality could be better"
]

keywords = ['great', 'quality', 'delivery']

all_feedback = " ".join(feedback).lower()
print(all_feedback)
print()

keyword_counts = {}
for keyword in keywords:
    keyword_counts[keyword] = all_feedback.count(keyword)

for keyword in keyword_counts:
    print(f"'{keyword}' appears {keyword_counts[keyword]} times")
