import os
import sys
import pytest
abspath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, abspath + '/../')

from reverse_dh import Solution

@pytest.fixture
def inst():
    return Solution()

def test_reverse(inst):
    c_inst = inst
    assert c_inst.reverse(123) == 321
    assert c_inst.reverse(-123) == -321
    assert c_inst.reverse(120) == 21
