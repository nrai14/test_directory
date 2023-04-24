import pytest 

from lib.password_checker import *

def test_password():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.check('1234567')
    error_message = str(e.value)
    assert error_message == 'Invalid password, must be 8+ characters.'

def test_password_valid():
    password_checker = PasswordChecker()
    result = password_checker.check('89101112131415')
    assert result == True