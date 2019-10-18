import unittest
from main import div_by_5, div_by_3

def test_div_by_3():
    assert div_by_3(3) == True


def test_div_by_5():
    assert div_by_5(5) == True


def test_div_by_5_and_3():
    assert (div_by_3(75) and div_by_3(75)) == True



if __name__ == "__main__":
    test_div_by_3()
    test_div_by_5()
    test_div_by_5_and_3()