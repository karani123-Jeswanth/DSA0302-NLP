from nltk.metrics.distance import edit_distance

# Small reference dictionary of correct words
vocab = [
    "this", "is", "a", "simple", "spell", "checker", 
    "program", "using", "natural", "language", "processing"
]

def spell_check(sentence):
    words = sentence.lower().split()
    corrected = []

    for word in words:
        if word in vocab:
            corrected.append(word)
        else:
            # Find the word in vocab with the lowest edit distance
            closest = min(vocab, key=lambda correct_word: edit_distance(word, correct_word))
            print(f"Typo detected: '{word}' -> Corrected to: '{closest}'")
            corrected.append(closest)

    return " ".join(corrected)

# Test with typos
text = "thiss is a simpl spel chekr"
print("Original :", text)
print("Corrected:", spell_check(text))