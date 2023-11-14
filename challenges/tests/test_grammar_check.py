from lib.grammar_check import *
import pytest

# Describe the problem

"""
As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and 
ends with a suitable sentence-ending punctuation mark.

"""

# function signature

"""
takes in a string
check that the first letter at index 0 is .upper()
check index[::-1] is a '.' - last char of full string, not last word
return bool?

"""


# test data type of the input raises an error if incorrect
def test_data_type():
    with pytest.raises(TypeError) as err:
        grammar_check(1)
        assert str(err.value) == "Incorrect data type"


# test that the function returns a bool
# test empty string input
def test_empty_string():
    result = grammar_check("")
    assert result == False


# test a single word with capital & . at the end is true
def test_correctly_inputted_text():
    result = grammar_check("Hello.")
    assert result == True


# test incorrect word returns false
def test_incorrect_first_letter_text():
    result = grammar_check("hello.")
    assert result == False


def test_incorrect_last_character():
    result = grammar_check("Hello")
    assert result == False


# test ! ? at the end of the string
def test_punctuation_alternatives():
    results = []
    for punctuation in ["!", "?"]:
        result = grammar_check(punctuation)
        results.append(result)
    assert results == [True, True]


# test long string
def test_longer_string_input():
    results = grammar_check("One two three four five six.")
    assert results == True
