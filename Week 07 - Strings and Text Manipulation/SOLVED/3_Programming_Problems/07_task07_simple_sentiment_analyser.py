positive_words = ['amazing', 'love', 'fantastic', 'great', 'excellent']
negative_words = ['terrible', 'worst', 'poor', 'awful', 'horrible']


def has_word(text, words):
    """Return True if any word from words is in text without "not " just before it."""
    return any(word in text and f"not {word}" not in text for word in words)


def analyse_sentiment(reviews):
    """Classify each review and return a dict of counts plus the list of negative reviews."""
    result = {"positive": 0, "negative": 0, "neutral": 0, "negative_reviews": []}

    for review in reviews:
        clean_review = review.strip().lower()
        is_positive = has_word(clean_review, positive_words)
        is_negative = has_word(clean_review, negative_words)

        if is_positive and not is_negative:
            label = "positive"
        elif is_negative and not is_positive:
            label = "negative"
            result["negative_reviews"].append(clean_review)
        else:
            label = "neutral"

        result[label] += 1
        print(f"{label:<9} <- {clean_review}")

    return result


reviews = [
    "  AMAZING product, Love it!!!  ",
    "terrible experience   ",
    "  It was okay  ",
    "WORST purchase ever",
    "  fantastic quality  ",
    "poor customer service",
    "  Not bad, not great  "
]

summary = analyse_sentiment(reviews)
print()
print(f"Positive: {summary['positive']}")
print(f"Negative: {summary['negative']}")
print(f"Neutral:  {summary['neutral']}")
print("Negative reviews:")
for review in summary["negative_reviews"]:
    print(f"  - {review}")
