"""
Word Occurrences
Estimate: 20 minutes
Actual:   13 minutes
"""

words = input("Text: ").split()
word_to_count = {}
for word in words:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1

max_word_length = max(len(word) for word in word_to_count.keys())
for word, count in sorted(word_to_count.items()):
    print(f"{word:{max_word_length}} : {count}")
