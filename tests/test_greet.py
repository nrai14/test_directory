from lib.greet import *

def test_greet():
    result = greet('Nish')
    assert result == "Hello, Nish!"