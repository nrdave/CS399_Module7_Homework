"""
Remove Outliers from a list of words
Author: Nikhil Dave
"""

from wv import Model
from scipy.stats import zscore

model = Model("models/glove_short.txt")
while True:
    words = input("Please enter a comma separated list of words: ").split(",")

    # Remove whitespace
    words = [w.strip() for w in words]
    modeled_words = [model.find_word(w) for w in words]
    # Check for minimum word count and that all words are modeled
    if len(words) < 3 or None in modeled_words:
        break

    print(*words, sep=", ", end=".\n")
