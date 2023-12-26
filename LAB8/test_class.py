import pytest
from triangle_class import Triangle, IncorrectTriangleSides


def test_valid_triangle_creation():
    triangle = Triangle(3, 4, 5)
    assert triangle.a == 3
    assert triangle.b == 4
    assert triangle.c == 5


def test_invalid_triangle_creation():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(1, 1, 2)


def test_equilateral_triangle_type():
    triangle = Triangle(5, 5, 5)
    assert triangle.triangle_type() == "equilateral"


def test_isosceles_triangle_type():
    triangle = Triangle(5, 5, 6)
    assert triangle.triangle_type() == "isosceles"


def test_nonequilateral_triangle_type():
    triangle = Triangle(3, 4, 5)
    assert triangle.triangle_type() == "nonequilateral"


def test_perimeter():
    triangle = Triangle(3, 4, 5)
    assert triangle.perimeter() == 12
