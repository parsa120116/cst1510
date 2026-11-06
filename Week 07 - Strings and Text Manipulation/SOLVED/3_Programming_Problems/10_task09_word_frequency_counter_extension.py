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


try:
    with open("DATA/Les_Brown.txt", encoding="utf-8") as file:
        content = file.read()
except FileNotFoundError:
    print("Could not find DATA/Les_Brown.txt - run this from the Programming_Problems folder.")
else:
    counts = word_frequency(content)
    print()
    print(f"{len(counts)} different words")
    print(f"'dream' appears {counts.get('dream', 0)} times")

    # Words that still contain something that is not a letter or an apostrophe
    messy_words = [word for word in counts if not word.replace("'", "").isalpha()]
    print("Words that still look messy:", messy_words)
