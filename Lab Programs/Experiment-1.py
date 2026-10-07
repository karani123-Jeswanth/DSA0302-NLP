from collections import Counter
from nltk.tokenize import sent_tokenize, word_tokenize

text = """Natural Language Processing (NLP) is a branch of artificial intelligence. 
It helps computers understand human language. NLP makes it possible for computers 
to read text and hear speech. Is NLP hard? Yes, but NLP is fascinating!"""

sentences = sent_tokenize(text)

words = [word.lower() for word in word_tokenize(text) if word.isalnum()]

total_word_count = len(words)

freq = Counter(words)
top_3 = freq.most_common(3)

print("=== (a) Sentences ===")
for idx, sentence in enumerate(sentences, 1):
    print(f"{idx}. {sentence}")

print("\n=== (b) Word Tokens ===")
print(words)

print(f"\n=== (c) Total Word Count: {total_word_count} ===")

print("\n=== (d) Most Frequent Words ===")
for word, count in top_3:
    print(f"'{word}': {count} time(s)")
