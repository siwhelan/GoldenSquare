import pytest
from lib.password_checker import *


# test 8 char password passes
def test_minimum_password_length():
    pword = PasswordChecker()
    new_pass = pword.check("password")
    assert new_pass == True


# test password with more than 8 characters passes
def test_long_password():
    pword = PasswordChecker()
    new_pass = pword.check("verylongpassword")
    assert new_pass == True


# test 7 char password fails
def test_short_password():
    pword = PasswordChecker()
    with pytest.raises(Exception) as err:
        pword.check("1234567")
    assert str(err.value) == "Invalid password, must be 8+ characters."


# test empty password fails
def test_empty_password():
    pword = PasswordChecker()
    with pytest.raises(Exception) as err:
        pword.check("")
    assert str(err.value) == "Invalid password, must be 8+ characters."
