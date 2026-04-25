import pytest
from string_manip import *  # Import functions from string_manip.py

def test_capitalize_words_basic_operations():
    assert capitalize_words("hello world") == "Hello World"
    assert capitalize_words("python programming") == "Python Programming"

def test_capitalize_words_empty_string():
    assert capitalize_words("") == ""

def test_capitalize_words_with_list():
    with pytest.raises(TypeError):
        capitalize_words(['hello', 'world'])  

def test_capitalize_words_with_tuple():
    with pytest.raises(TypeError):
        capitalize_words(('hello', 'world'))  

def test_capitalize_words_with_object():
    with pytest.raises(TypeError):
        capitalize_words(object())  

def test_capitalize_words_with_none():
    with pytest.raises(TypeError):
        capitalize_words(None)  

def test_capitalize_words_with_bytearray():
    with pytest.raises(TypeError):
        capitalize_words(bytearray(b"hello world"))  


# --- reverse_string ---

def test_reverse_string_basic():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("Python") == "nohtyP"

def test_reverse_string_empty():
    assert reverse_string("") == ""

def test_reverse_string_palindrome_unchanged():
    assert reverse_string("racecar") == "racecar"

def test_reverse_string_type_error():
    with pytest.raises(TypeError):
        reverse_string(123)

def test_reverse_string_type_error_none():
    with pytest.raises(TypeError):
        reverse_string(None)


# --- count_vowels ---

def test_count_vowels_basic():
    assert count_vowels("hello") == 2
    assert count_vowels("aeiou") == 5

def test_count_vowels_uppercase():
    assert count_vowels("AEIOU") == 5

def test_count_vowels_mixed_case():
    assert count_vowels("Hello World") == 3

def test_count_vowels_no_vowels():
    assert count_vowels("gym") == 0

def test_count_vowels_empty():
    assert count_vowels("") == 0

def test_count_vowels_type_error():
    with pytest.raises(TypeError):
        count_vowels(42)


# --- is_palindrome ---

def test_is_palindrome_true():
    assert is_palindrome("racecar") is True
    assert is_palindrome("madam") is True

def test_is_palindrome_false():
    assert is_palindrome("hello") is False

def test_is_palindrome_case_insensitive():
    assert is_palindrome("RaceCar") is True

def test_is_palindrome_ignores_spaces():
    assert is_palindrome("a man a plan a canal panama") is True

def test_is_palindrome_empty():
    assert is_palindrome("") is True

def test_is_palindrome_type_error():
    with pytest.raises(TypeError):
        is_palindrome(["r", "a", "c", "e"])


# --- truncate ---

def test_truncate_basic():
    assert truncate("Hello, World!", 5) == "Hello..."

def test_truncate_no_truncation_needed():
    assert truncate("Hi", 10) == "Hi"

def test_truncate_exact_length():
    assert truncate("Hello", 5) == "Hello"

def test_truncate_empty_string():
    assert truncate("", 5) == ""

def test_truncate_type_error_not_string():
    with pytest.raises(TypeError):
        truncate(12345, 3)

def test_truncate_value_error_negative_length():
    with pytest.raises(ValueError):
        truncate("hello", -1)

