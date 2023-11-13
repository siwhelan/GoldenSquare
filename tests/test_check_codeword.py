from lib.check_codeword import *


# check return with correct word
def test_correct_word():
    result = check_codeword("horse")
    assert result == "Correct! Come in."


# check return witrh incorrect word


def test_incorrect_word():
    result = check_codeword("Barbara")
    assert result == "WRONG!"


# check return with a 'close' word


def test_close_word():
    result = check_codeword("house")
    assert result == "Close, but nope."


# Check first letter wrong
def test_incorrect_first_letter():
    result = check_codeword("mouse")
    assert result == "WRONG!"


# Check last letter wrong
def test_incorrect_last_letter():
    result = check_codeword("horses")
    assert result == "WRONG!"
