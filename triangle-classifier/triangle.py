"""Triangle classifier."""

import math

# Relative tolerance used when checking the Pythagorean theorem, so that
# floating-point sides like (1, 1, sqrt(2)) are still recognised as right.
RIGHT_ANGLE_TOLERANCE = 1e-9


def is_valid_triangle(a, b, c) -> bool:
    """Return True if a, b, c can form a (non-degenerate) triangle.

    All sides must be positive, and the sum of any two sides must be
    strictly greater than the third. If two sides add up to exactly the
    third side, the triangle is degenerate and counts as invalid.
    """
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return a + b > c and a + c > b and b + c > a


def _is_right(a, b, c) -> bool:
    """Return True if the sides satisfy the Pythagorean theorem (within tolerance)."""
    x, y, z = sorted((a, b, c))  # z is the longest side (hypotenuse candidate)
    return math.isclose(x * x + y * y, z * z, rel_tol=RIGHT_ANGLE_TOLERANCE)


def classify_triangle(a, b, c) -> str:
    """Classify a triangle by its sides.

    Returns "Invalid", "Equilateral", "Isosceles" or "Scalene".
    Right triangles get the prefix "Right ", e.g. "Right Scalene".
    """
    if not is_valid_triangle(a, b, c):
        return "Invalid"

    if a == b == c:
        kind = "Equilateral"
    elif a == b or b == c or a == c:
        kind = "Isosceles"
    else:
        kind = "Scalene"

    if _is_right(a, b, c):
        return "Right " + kind
    return kind
