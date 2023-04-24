import pytest
from lib.present import *

def test_wrap_unwrap_present():
    present = Present()
    present.wrap(20)
    assert present.unwrap() == 20

def test_unwrap_present_without_wrap():
    present = Present()

    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."

def test_wrap_twice():
    present = Present()

    with pytest.raises(Exception) as e:
        present.wrap(2)
        present.wrap(4)
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."