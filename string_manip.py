def capitalize_words(text):
    """
    Capitalizes the first letter of each word in the given text.
    Raises a TypeError if the input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return " ".join(word.capitalize() for word in text.split())


def reverse_string(text):
    """
    Returns the reverse of the given string.
    Raises a TypeError if the input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return text[::-1]


def count_vowels(text):
    """
    Returns the number of vowels (a, e, i, o, u) in the given string.
    Raises a TypeError if the input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return sum(1 for ch in text if ch.lower() in "aeiou")


def is_palindrome(text):
    """
    Returns True if the string reads the same forwards and backwards,
    ignoring case and spaces. Raises a TypeError if input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def truncate(text, max_length):
    """
    Truncates text to max_length characters, appending '...' if shortened.
    Raises TypeError if text is not a string; ValueError if max_length < 0.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    if max_length < 0:
        raise ValueError("max_length must be a non-negative integer")
    if len(text) <= max_length:
        return text
    return text[:max_length] + "..."
