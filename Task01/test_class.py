import pytest
from triangle_class import Triangle, IncorrectTriangleSides


def test_equilateral_triangle():
    t = Triangle(3, 3, 3)
    assert t.triangle_type() == "equilateral"
    assert t.perimeter() == 9


def test_isosceles_triangle():
    t = Triangle(5, 5, 3)
    assert t.triangle_type() == "isosceles"
    assert t.perimeter() == 13


def test_nonequilateral_triangle():
    t = Triangle(3, 4, 5)
    assert t.triangle_type() == "nonequilateral"
    assert t.perimeter() == 12

def test_invalid_triangle_sides():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(1, 2, 3)


def test_zero_side():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(0, 2, 2)


def test_negative_side():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(-1, 2, 2)


def test_wrong_type():
    with pytest.raises(IncorrectTriangleSides):
        Triangle("3", 3, 3)
