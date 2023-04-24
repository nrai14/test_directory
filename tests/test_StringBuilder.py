from lib.string_builder import *

def test_string_builder_jamaica():
    string_builder = StringBuilder()
    string_builder.add('jamaica')
    result = string_builder.size()
    assert result == 7
    result1 = string_builder.output()
    assert result1 == 'jamaica'