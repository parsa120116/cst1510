def word_frequency(text):
    """Return a dict of word -> count for text, and print the 5 most common words."""
    clean_text = text.lower()
    for mark in [".", ",", "!", "?"]:
        clean_text = clean_text.replace(mark, "")

    words = clean_text.split()

    frequency = {}
    for word in words:
        if word not in frequency:
            frequency[word] = words.count(word)

    ranked_words = sorted(frequency, key=frequency.get, reverse=True)
    print("Top 5 words:")
    for word in ranked_words[:5]:
        print(f"  {word}: {frequency[word]}")

    return frequency


text = """Data science is the study of data. Data scientists use data to find patterns.
Machine learning is a part of data science. Scientists study data every day!
The science of data is growing, and data is everywhere."""

counts = word_frequency(text)
print()
print(f"{len(counts)} different words")
print(counts)
