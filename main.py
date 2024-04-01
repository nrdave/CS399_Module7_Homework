"""
Remove Outliers from a list of words
Author: Nikhil Dave
"""

from wv import Model
from scipy.stats import zscore

model = Model("models/glove_short.txt")
while True:
    words = input("Please enter a comma separated list of words: ").split(",")

    if len(words) < 3:
        break

    words = [w.strip() for w in words]

    print(*words, sep=", ", end=".\n")
