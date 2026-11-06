with open("DATA/Les_Brown.txt") as file:
    text = file.read()

word_counts = {}
for raw_word in text.split():
    word = raw_word.strip('.,!?:;"').lower()     # "Dream!" -> "dream"
    if word == "":
        continue
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

with open("word_count.txt", "w") as out_file:
    for word in sorted(word_counts):
        out_file.write(f"{word}: {word_counts[word]}\n")

print(f"{len(word_counts)} different words saved to word_count.txt")

# Bonus: the 5 most common words
pairs = [(count, word) for word, count in word_counts.items()]
pairs.sort(reverse=True)
print("Top 5 words:")
for count, word in pairs[:5]:
    print(f"  {word}: {count}")
