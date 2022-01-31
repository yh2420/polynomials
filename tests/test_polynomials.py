from polynomials import Polynomial
import pytest

def test_print():

    p = Polynomial((2, 1, 0, 3))

    assert str(p) == "3x^3 + x + 2"  # 和print()类似，对但是这个输出是string，有‘’

def test_equality():
    assert Polynomial((0,1)) == Polynomial((0,1))

'''
@pytest.mark.parametrize(
    "a, b, sum"
    (((0,), (0,1), (0,1)),  # 每行前两个括号代表的polynomial之和等于最后一个
    ((2,0,3), (1,2), (3,2,3)),
    (4,2), (10,2,4), (14,4,4)))
    )
'''

def test_add(a, b, sum):
    assert Polynomial(a) + Polynomial(b) == Polynomial(sum)

def test_add_scalar():
    assert Polynomial((2,1) + 3) == Polynomial((5,1))

def test_add_unknown():
    with pytest.raises(TypeError):  # 出来TypeError结果才算True
        Polynomial((1,)) + "frog"

