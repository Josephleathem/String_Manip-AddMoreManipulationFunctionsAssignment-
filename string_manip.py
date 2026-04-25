def capitalize_words(text):
    """
    Capitalizes the first letter of each word in the given text.
    Raises a TypeError if the input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return " ".join(word.capitalize() for word in text.split())
