import os
import sys
import pytest
abspath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, abspath + '/../')

from reverse_dh import Solution as dh_S
from reverse_dy import Solution as dy_S

@pytest.fixture
def inst():
    return dh_S(), dy_S()

def test_reverse_dh(inst):
    dh_inst, _ = inst
    assert dh_inst.reverse(123) == 321
    assert dh_inst.reverse(-123) == -321
    assert dh_inst.reverse(120) == 21

def test_reverse_dy(inst):
    _, dy_inst = inst 
    assert dy_inst.reverse(123) == 321
    assert dy_inst.reverse(-123) == -321
    assert dy_inst.reverse(120) == 21

