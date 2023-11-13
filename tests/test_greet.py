from lib.greet import *

# Test the return is as expected


def test_greeting():
    result = greet("Simon")
    assert result == "Hello, Simon!"
