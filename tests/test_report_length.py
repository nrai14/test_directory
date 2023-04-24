from lib.report_length import *

def test_report_length():
    result = report_length('long')
    assert result == "This string was 4 characters long."

def test_report_length1():
    result = report_length('Hello! You!')
    assert result == "This string was 11 characters long."

