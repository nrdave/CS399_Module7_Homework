"""
Remove Outliers from a list of words

This program uses a subset of the Stanford GloVe model to find and remove
outliers in a list of words.
Author: Nikhil Dave
"""

from wv import Model
from scipy.stats import zscore

model = Model("model.txt")


def remove_outliers(words: list[str]) -> list[str]:
    """
    Use the loaded model to remove outliers from a list of words

    This function takes in a list of words and, using a given word to vector
    model (currently Stanford's GloVe), removes "outliers".
    """
    modeled_words = [model.find_word(w) for w in words]
    # Check for minimum word count and that all words are modeled
    if len(words) < 3 or None in modeled_words:
        return []
    for w in modeled_words:
        w.normalize()

    zscores = [
        abs(z)
        for z in zscore(
            [
                sum([word.similarity(w2)
                    for w2 in modeled_words if w2 is not word])
                for word in modeled_words
            ]
        )
    ]
    ZSCORE_THRESHOLD = 1.2
    words = [w for w, z in zip(words, zscores) if abs(z) < ZSCORE_THRESHOLD]
    return words


def main():
    """
    Remove outliers from a list of words provided through the terminal

    This function takes a list of words from the user typed from the running
    terminal and removes the outlier words
    """
    while True:
        try:
            words = input(
                "Please enter a comma separated list of words: ").split(",")
            # Remove whitespace
            words = [w.strip() for w in words]
            filtered_words = remove_outliers(words)
            if not filtered_words:
                break

            print(*filtered_words, sep=", ", end=".\n")

        except EOFError:
            print("\n")
            break


if __name__ == "__main__":
    main()
