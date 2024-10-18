"""
Word Occurrences
Estimate: 20 minutes
Actual:   ?? minutes
"""

words = input("Text: ").split()
word_to_count = {}
for word in words:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1

for word, count in sorted(word_to_count.items()):
    print(f"{word} : {count}")
