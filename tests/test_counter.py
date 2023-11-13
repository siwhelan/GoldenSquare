from lib.counter import *


# test initial state is 0
def test_starts_at_zero():
    counter = Counter()
    assert counter.report() == "Counted to 0 so far."


# test add
def test_add_number():
    counter = Counter()
    counter.add(5)
    assert counter.report() == "Counted to 5 so far."


# test add multiple numbers
def test_add_multiple_numbers():
    counter = Counter()
    counter.add(5)
    counter.add(5)
    counter.add(5)
    assert counter.report() == "Counted to 15 so far."
