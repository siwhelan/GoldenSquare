from lib.text_check import *
import pytest

"""
As a user
So that I can keep track of my tasks
I want to check if a text includes the string "#TODO".

"""

"""
function - text_check()
input should be 'text' / string
output True if the text includes "#TODO" and false if not

"""


# test incorrect type?
def test_incorrect_input_data_type():
    with pytest.raises(TypeError) as err:
        result = text_check(0)
    assert str(err.value) == "Incorrect data type"


# test correct input type of empty string
def test_empty_string_input():
    result = text_check("")
    assert result == False


# returns true if text includes example
def test_return_true_string_contains_TODO():
    result = text_check("#TODO")
    assert result == True


# text #todo in middle of the string
def test_todo_in_middle_of_the_string():
    result = text_check("word word2 three #TODO four")
    assert result == True


# test long string with no TODFO returns false
def test_long_string_no_todo():
    result = text_check("word word2 three four")
    assert result == False
