from lib.speed_reader import *

"""
As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

# test return data type is a string
# def test_function_returns_a_string():
#     assert type(speed_reader()) == str


# test a text of 200 words returns 1 minute
def test_function_calculates_200_words():
    assert speed_reader(200) == "1"


# test a text of 400 words returns 2 minutes
def test_function_calculates_400_words():
    assert speed_reader(400) == "2"

# test a text of 300 words returns 2 minutes
def test_function_calculates_400_words():
    assert speed_reader(400) == "1.5"

"""


# test a text of 200 words returns 1 minute
def test_function_calculates_200_words():
    text = " ".join(["word" for word in range(0, 200)])
    result = speed_reader(text)
    assert result == 1


# test a text of 400 words returns 2 minutes
def test_function_calculates_400_words():
    text = " ".join(["word" for word in range(0, 400)])
    result = speed_reader(text)
    assert result == 2


# test a text of 300 words returns 2 minutes
def test_function_calculates_300_words():
    text = " ".join(["word" for word in range(0, 300)])
    result = speed_reader(text)
    assert result == 1.5
