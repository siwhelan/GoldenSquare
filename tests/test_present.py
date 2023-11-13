import pytest
from lib.present import *


# test initial state is None
def test_initial_state():
    present = Present()
    assert present.contents is None


# test wrapping present
def test_wrap():
    present = Present()
    present.wrap("Gift")
    assert present.contents == "Gift"


# test for attempting to wrap contents twice
def test_wrap_twice():
    p = Present()
    p.wrap("Gift")
    with pytest.raises(Exception) as err:
        p.wrap("Second Gift")
    assert str(err.value) == "A contents has already been wrapped."


# test for attempting to unwrap empty present
def test_unwrap_empty_present():
    p = Present()
    with pytest.raises(Exception) as err:
        p.unwrap()
    assert str(err.value) == "No contents have been wrapped."
