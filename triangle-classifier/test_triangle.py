import math

import pytest

from triangle import classify_triangle, is_valid_triangle


@pytest.mark.parametrize(
    ("sides", "expected"),
    [
        ((4, 4, 4), "Equilateral"),
        ((2, 2, 3), "Isosceles"),
        ((4, 5, 6), "Scalene"),
        ((3, 4, 5), "Right Scalene"),
        ((0, 2, 2), "Invalid"),
    ],
)
def test_triangle_classification(sides, expected):
    assert classify_triangle(*sides) == expected


def test_degenerate_triangle_is_invalid():
    assert is_valid_triangle(1, 2, 3) is False
    assert classify_triangle(1, 2, 3) == "Invalid"


def test_negative_side_is_invalid():
    assert is_valid_triangle(-1, 2, 2) is False
    assert classify_triangle(-1, 2, 2) == "Invalid"


def test_right_isosceles_with_non_integer_hypotenuse():
    assert classify_triangle(5, 5, 5 * math.sqrt(2)) == "Right Isosceles"


def test_equilateral_triangle_is_not_right():
    assert classify_triangle(5, 5, 5) == "Equilateral"
