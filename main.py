"""
Remove Outliers from a list of words

This program uses a subset of the Stanford GloVe model to find and remove
outliers in a list of words.
Author: Nikhil Dave
"""

from wv import Model
from scipy.stats import zscore

model = Model("models/glove_short.txt")


def remove_outliers(words: list[str]) -> list[str]:
    # Remove whitespace
    words = [w.strip() for w in words]
    modeled_words = [model.find_word(w) for w in words]
    # Check for minimum word count and that all words are modeled
    if len(words) < 3 or None in modeled_words:
        return []
    for w in modeled_words:
        w.normalize()

    zscores = zscore(
        [
            sum([word.similarity(w2)
                for w2 in modeled_words if w2 is not word])
            for word in modeled_words
        ]
    )
    zscores = [abs(z) for z in zscores]

    ZSCORE_THRESHOLD = 1.2

    words = [w for w, z in zip(words, zscores) if abs(z) < ZSCORE_THRESHOLD]

    return words


def main():
    while True:
        try:
            words = input(
                "Please enter a comma separated list of words: ").split(",")
        except EOFError:
            break

        filtered_words = remove_outliers(words)
        if not filtered_words:
            break

        print(*filtered_words, sep=", ", end=".\n")


if __name__ == "__main__":
    main()
