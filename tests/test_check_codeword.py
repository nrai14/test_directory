from lib.check_codeword import *

def test_check_codeword():
    result = check_codeword('horse')
    assert result == 'Correct! Come in.'


def test_check_codeword1():
    result = check_codeword('hose')
    assert result == 'Close, but nope.'

def test_check_codeword2():
    result = check_codeword('chicken')
    assert result == 'WRONG!'


