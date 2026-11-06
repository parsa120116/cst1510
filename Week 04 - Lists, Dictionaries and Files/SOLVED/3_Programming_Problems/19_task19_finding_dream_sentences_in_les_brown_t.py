with open("DATA/Les_Brown.txt") as file:
    text = file.read()

# The file is cut into lines of ~90 characters, so first make it one long text
text = text.replace("\n", " ")

# Split into sentences: a sentence ends at . ! or ?
sentences = []
current = ""
for char in text:
    if char == '"' and current == "" and len(sentences) > 0:
        sentences[-1] += char      # a closing quote right after ! belongs to the last sentence
        continue
    current += char
    if char in ".!?":
        sentences.append(current)
        current = ""
if current.strip() != "":
    sentences.append(current)      # the last piece may have no end mark

# Keep only the sentences with "dream" (case-insensitive)
dream_sentences = []
for sentence in sentences:
    clean_sentence = " ".join(sentence.split())    # remove extra spaces
    if "dream" in clean_sentence.lower():
        dream_sentences.append(clean_sentence)

with open("dream_sentences.txt", "w") as out_file:
    for sentence in dream_sentences:
        out_file.write(sentence + "\n")

print(f"Found {len(dream_sentences)} sentences with 'dream' (saved to dream_sentences.txt):")
for sentence in dream_sentences:
    print("-", sentence)
