from lib.count_words import *


# takes an empty string, and returns an empty string
def test_empty_string_returns_empty_string():
    word = count_words("")
    assert word == ""


# takes a single word and returns the number of words
def test_single_word_input_and_output():
    word_count = count_words("one")
    assert word_count == 1


# takes multiple words and returns the number count
def test_multiple_word_input_and_output():
    word_count = count_words("one two three for five")
    assert word_count == 5


# Test with leading and trailing spaces
def test_input_with_spaces():
    word_count = count_words("   word   ")
    assert word_count == 1


# Test with tabs and newlines as separators
def test_input_with_tabs_and_newlines():
    word_count = count_words("one\ttwo\nthree")
    assert word_count == 3


# Test with multiple spaces between words
def test_input_with_multiple_spaces():
    word_count = count_words("one  two   three")
    assert word_count == 3


# Test with mixed input of words and numbers
def test_mixed_input():
    word_count = count_words("one 2 three 4 five")
    assert word_count == 5
