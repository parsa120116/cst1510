PUNCTUATION = '.,!?;:"()'


def get_score(result):
    """Return the score of one search result (used for sorting)."""
    return result["score"]


def search(documents, query):
    """Rank documents by how many times the query words appear; print and return the results."""
    query_words = query.lower().strip().split()
    results = []

    for document in documents:
        clean_document = document.lower()
        for mark in PUNCTUATION:
            clean_document = clean_document.replace(mark, " ")
        document_words = clean_document.split()

        # Skip documents that contain none of the query words
        if not any(word in document_words for word in query_words):
            continue

        score = 0
        found = []
        for word in query_words:
            hits = document_words.count(word)
            if hits > 0:
                score += hits
                found.append(f"{word} x{hits}")

        # Highlight: put [ ] around every word of the document that matches the query
        highlighted = []
        for original_word in document.split():
            if original_word.lower().strip(PUNCTUATION) in query_words:
                highlighted.append(f"[{original_word}]")
            else:
                highlighted.append(original_word)

        results.append({
            "document": document,
            "score": score,
            "found": found,
            "all_found": all(word in document_words for word in query_words),
            "highlighted": " ".join(highlighted),
        })

    results.sort(key=get_score, reverse=True)

    print(f'Search: "{query}"  ->  {len(results)} matching document(s)')
    rank = 1
    for result in results:
        if result["all_found"]:
            tag = "  (all words found)"
        else:
            tag = ""
        print(f"{rank}. score {result['score']} | found: {', '.join(result['found'])}{tag}")
        print(f"   {result['highlighted']}")
        rank += 1
    print()
    return results


documents = [
    "Python is a great programming language for data science and machine learning",
    "Data analysis with Python involves cleaning and processing large datasets",
    "Machine learning models can predict outcomes from historical data",
    "Web development with JavaScript and HTML is different from data work",
    "Python data science libraries include NumPy and Pandas for data processing"
]

# Test searches
search(documents, "data science")
search(documents, "Python machine learning")
search(documents, "cooking")
