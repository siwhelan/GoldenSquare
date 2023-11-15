import pytest
from lib.class_diary_entry import *


# Test that the programme raises an error when given an empty title
def test_empty_title_raises_error():
    with pytest.raises(Exception) as err:
        DiaryEntry("", "new content")
    assert str(err.value) == "Missing Data!"


# Test that the programme raises an error when given empty contents
def test_empty_contents_raises_error():
    with pytest.raises(Exception) as err:
        DiaryEntry("new title", "")
    assert str(err.value) == "Missing Data!"


# Test .format() returns a correctly formatted input,
# e.g. "My Title: These are the contents"
def test_format_title_and_contents():
    entry1 = DiaryEntry("Title1", "Insert contents here")
    result = entry1.format()
    assert result == "Title1: Insert contents here"


# Test .count_words returns the number of words in the diary entry
def test_count_words_in_contents():
    contents = DiaryEntry("New title", "new content")
    result = contents.count_words()
    assert result == 4


# Given a wpm of 0, reading_time raises an error
def test_reading_time_at_zero_wpm():
    new_entry = DiaryEntry("Reading Time Test 4", "three word test")
    with pytest.raises(Exception) as err:
        new_entry.reading_time(0)
    assert str(err.value) == "Unable to calculate reading time. Please re-enter."


# Given a wpm of 2 and a text with 2 words, test that reading_time returns '1 minute'
def test_reading_time_at_2wpm_and_two_words():
    new_entry = DiaryEntry("Reading Time Test 1", "two words")
    reading_time = new_entry.reading_time(2)
    assert reading_time == 1


# Given a wpm of 2 and a text with 4 words, test that reading_time returns '2 minutes'
def test_reading_time_at_2wpm_and_four_words():
    new_entry = DiaryEntry("Reading Time Test 2", "two words two times")
    reading_time = new_entry.reading_time(2)
    assert reading_time == 2


# Given a wpm of 2 and a text with 3 words, test that reading_time returns '2 minutes'
# #(rounding up)
def test_reading_time_at_2wpm_and_three_words():
    new_entry = DiaryEntry("Reading Time Test 3", "three word test")
    reading_time = new_entry.reading_time(2)
    assert reading_time == 2


#   wpm: an integer representing the number of words the user can read
#        per minute
#   minutes: an integer representing the number of minutes the user has
#            to read
# Returns:
#   string: a chunk of the contents that the user could read in the
#           given number of minutes
#
# If called again, `reading_chunk` should return the next chunk,
# skipping what has already been read, until the contents is fully read.
# The next call after that should restart from the beginning.


# With a contents of 6 words and a wpm of 2
# plus a 'minutes' of 2, reading_chunk returns the first 2 words
def test_reading_chunk_with_two_wpm_and_one_minute():
    new_entry = DiaryEntry("New Title", "one two three four five six")
    result = new_entry.reading_chunk(2, 1)
    assert result == "one two"


# With a contents of 6 words and a wpm of 2
# plus a 'minutes' of 2, reading_chunk returns the first 4 words
def test_reading_chunk_with_two_wpm_and_two_minutes():
    new_entry = DiaryEntry("New Title", "one two three four five six")
    result = new_entry.reading_chunk(2, 2)
    assert result == "one two three four"


# With a contents of 6 words and a wpm of 2
# plus a 'minutes' of 1, reading_chunk returns the first 2 words
# on the first call, second chunk on the second call etc
def test_reading_chunks_with_two_wpm_and_one_minute_called_twice():
    new_entry = DiaryEntry("New Title", "one two three four five six")
    assert new_entry.reading_chunk(2, 1) == "one two"
    assert new_entry.reading_chunk(1, 1) == "three"
    assert new_entry.reading_chunk(2, 1) == "four five"


# Given 6 words, reading_chunk loops through the string
# if called repeatedly, starting at zero once the string has been completed
# and it is called again.
def test_reading_chunk_loops_contents_when_called_repeatedly():
    new_entry = DiaryEntry("New Title", "one two three four five six")
    assert new_entry.reading_chunk(2, 2) == "one two three four"
    assert new_entry.reading_chunk(2, 2) == "five six"
    assert new_entry.reading_chunk(2, 2) == "one two three four"
