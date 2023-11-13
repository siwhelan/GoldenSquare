from lib.string_builder import *


# test initial state is empty string
def test_initial_state():
    result = StringBuilder()
    assert result.output() == ""


# test adding single string returns correct output
def test_add_single_string():
    result = StringBuilder()
    result.add("house")
    assert result.output() == "house"


# test adding multiple strings returns correct output
def test_add_multiple_strings():
    result = StringBuilder()
    result.add("Hi ")
    result.add("frens")
    result.add("!")
    assert result.output() == "Hi frens!"


# test adding single string returns correct length
def test_add_single_string():
    result = StringBuilder()
    result.add("house")
    assert result.size() == 5


# test adding multiple strings returns correct length
def test_add_multiple_strings():
    result = StringBuilder()
    result.add("Hi ")
    result.add("frens")
    result.add("!")
    assert result.size() == 9
