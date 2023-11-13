from lib.make_snippet import *


# test empty string returns empty string
def test_empty_string():
    result = make_snippet("")
    assert result == ""


# test string with less than 5 words is returned in full
def test_short_string_is_returned_in_full():
    result = make_snippet("three worded string")
    assert result == "three worded string"


# test 5 word string is returned in full
def test_snippet_returns_five_words():
    my_string = make_snippet("these five words to test")
    assert my_string == "these five words to test"


# test 6 word string is returned with '...' after 5 words
def test_snippet_returns_long_string_and_dots():
    my_string = make_snippet("there's six words in this string")
    assert my_string == "there's six words in this ..."
