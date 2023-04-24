from lib.counter import *

def test_counter_3():
    counter = Counter()
    counter.add(3)
    result = counter.report()
    assert result == "Counted to 3 so far." 

def test_counter_76():
    counter = Counter()
    counter.add(76)
    result = counter.report()
    assert result == "Counted to 76 so far."