STOP_WORDS = ['the', 'a', 'is', 'and', 'of', 'to', 'in']
PUNCTUATION = '.,!?;:"()-*'
WIDTH = 46


def text_report(text):
    """Print a formatted analysis report of text."""
    # ---- 1. Basic stats
    total_characters = len(text)
    raw_words = text.split()
    total_sentences = text.count(".") + text.count("!") + text.count("?")

    clean_words = []
    for raw_word in raw_words:
        word = raw_word.strip(PUNCTUATION).lower()
        if word != "":
            clean_words.append(word)

    total_letters = 0
    for word in clean_words:
        total_letters += len(word)
    average_length = total_letters / len(clean_words)

    # ---- 2. Character breakdown
    uppercase = 0
    lowercase = 0
    digits = 0
    spaces = 0
    punctuation = 0
    for char in text:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1
        elif char.isdigit():
            digits += 1
        elif char.isspace():
            spaces += 1
        else:
            punctuation += 1

    # ---- 3. Top 5 words (without the stop words)
    word_counts = {}
    for word in clean_words:
        if word in STOP_WORDS:
            continue
        word_counts[word] = word_counts.get(word, 0) + 1
    top_words = sorted(word_counts, key=word_counts.get, reverse=True)[:5]

    # ---- 4. Longest and shortest words
    longest = clean_words[0]
    shortest = clean_words[0]
    for word in clean_words:
        if len(word) > len(longest):
            longest = word
        if len(word) < len(shortest):
            shortest = word

    # ---- 5. The report
    print("=" * WIDTH)
    print("TEXT REPORT".center(WIDTH))
    print("=" * WIDTH)

    print("Basic stats".center(WIDTH, "-"))
    print("Characters:".ljust(28) + str(total_characters))
    print("Words:".ljust(28) + str(len(raw_words)))
    print("Sentences:".ljust(28) + str(total_sentences))
    print("Average word length:".ljust(28) + f"{average_length:.2f}")

    print("Character breakdown".center(WIDTH, "-"))
    print("Uppercase letters:".ljust(28) + str(uppercase))
    print("Lowercase letters:".ljust(28) + str(lowercase))
    print("Digits:".ljust(28) + str(digits))
    print("Spaces (incl. newlines):".ljust(28) + str(spaces))
    print("Punctuation/other:".ljust(28) + str(punctuation))

    print("Top 5 words".center(WIDTH, "-"))
    print("In one line: " + ", ".join(top_words))
    for rank in range(len(top_words)):
        word = top_words[rank]
        print(f"{rank + 1}. " + word.ljust(25) + str(word_counts[word]))

    print("Longest and shortest".center(WIDTH, "-"))
    print("Longest word:".ljust(28) + f"{longest} (length {len(longest)})")
    print("Shortest word:".ljust(28) + f"{shortest} (length {len(shortest)})")
    print("=" * WIDTH)


corpus = """Artificial Intelligence is transforming every industry. From healthcare to finance,
AI systems are making decisions that affect millions of people. Machine Learning,
a subset of AI, enables computers to learn from data without being explicitly programmed.
Deep Learning takes this further with neural networks inspired by the human brain.
In 2024, Large Language Models like GPT have shown remarkable abilities in understanding
and generating human language. The future of AI is both exciting and challenging."""

text_report(corpus)
