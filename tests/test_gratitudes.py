from lib.gratitudes import *


# starts with an empty list
def test_check_initial_state():
    gratitude = Gratitudes()
    assert gratitude.format() == "Be grateful for: "


# test the add method adds the string to the list
def test_add_to_list():
    gratitude = Gratitudes()
    gratitude.add("food")
    assert gratitude.format() == "Be grateful for: food"


# test adding mulitple strings
def test_adding_multiple_strings():
    gratitude = Gratitudes()
    gratitude.add("food")
    gratitude.add("health")
    gratitude.add("family")
    gratitude.add("beer")
    assert gratitude.format() == "Be grateful for: food, health, family, beer"
