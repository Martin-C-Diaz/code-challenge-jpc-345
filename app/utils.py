import re


def transform_word(word: str) -> str:
    """
    Build a transform function for any string it receives converting it
    into a specif and defined format.

    :param word: word string to be formated
    :return: formated word if needed
    """
    # Base case
    if not word.isalpha():
        return word
    else:
        # Count how many characters are between the first and the last one.
        distinct_chars = len(set(word[1:-1]))
        # Return the word formated as expected.
        return str(f"{word[0]}{distinct_chars}{word[-1]}")


def parse_and_transform(sentence: str) -> str:
    """
    Convert a string sentence into a new with the specified format.

    :param sentence: sentece string to be formated
    :return: formated sentence
    """
    if isinstance(sentence, str):

        # Split the sentence into substrings based on non-alphabetic characters.
        substrings = re.split(r"([^a-zA-Z]+)", sentence)

        # Transform each substring and join them back together.
        transformed_substrings = [transform_word(substring) for substring in substrings]

        # return the formated sentence as string.
        return "".join(transformed_substrings)
