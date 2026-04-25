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

