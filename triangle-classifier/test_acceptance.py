"""Acceptance test for the stained-glass studio's triangle checker.

Customer requirement:
    "Customers enter three side lengths and we tell them the shape and
    whether it's buildable. If it's not a valid triangle, show a message,
    don't crash. Also flag right-angle pieces - they need reinforced
    corners. It has to be correct every time; a wrong answer means a
    ruined pane."

Acceptance criteria:
    AC1 (correct every time): for every order in the reference table below,
        in all 6 orderings of its sides, classify_triangle() returns exactly
        the expected label. Pass mark: 0 mismatches.
    AC2 (not buildable -> message, no crash): for every order with a side
        <= 0 or failing the triangle inequality (including two sides summing
        exactly to the third), classify_triangle() returns "Invalid" and
        raises no exception.
    AC3 (flag reinforced corners): a result starts with "Right " if and only
        if the sides satisfy a^2 + b^2 = c^2 (within a relative tolerance of
        1e-9). Pieces that are close to right but not right are not flagged.
"""

import math
from itertools import permutations

from triangle import classify_triangle

# A day of customer orders: (sides, expected label, criterion it exercises).
CUSTOMER_ORDERS = [
    # Buildable pieces (AC1)
    ((30, 30, 30), "Equilateral", "AC1"),
    ((25, 25, 40), "Isosceles", "AC1"),
    ((20, 30, 40), "Scalene", "AC1"),
    ((12.5, 12.5, 12.5), "Equilateral", "AC1"),
    # Right-angle pieces that need reinforced corners (AC3)
    ((30, 40, 50), "Right Scalene", "AC3"),
    ((0.3, 0.4, 0.5), "Right Scalene", "AC3"),
    ((10, 10, 10 * math.sqrt(2)), "Right Isosceles", "AC3"),
    # Close to right but not right: must not be flagged (AC3)
    ((30, 40, 50.01), "Scalene", "AC3"),
    # Not buildable: must show a message, not crash (AC2)
    ((0, 20, 20), "Invalid", "AC2"),
    ((-5, 20, 20), "Invalid", "AC2"),
    ((10, 20, 30), "Invalid", "AC2"),  # flat: 10 + 20 == 30
    ((5, 10, 40), "Invalid", "AC2"),
    ((-3, 4, 5), "Invalid", "AC2"),  # satisfies Pythagoras, still invalid
]


def test_studio_orders_are_classified_correctly_every_time():
    mismatches = []
    for sides, expected, criterion in CUSTOMER_ORDERS:
        for ordering in set(permutations(sides)):
            try:
                result = classify_triangle(*ordering)
            except Exception as exc:  # AC2: a crash is a failure, not an error
                mismatches.append(f"{criterion} {ordering}: raised {exc!r}")
                continue
            if result != expected:
                mismatches.append(
                    f"{criterion} {ordering}: expected {expected!r}, got {result!r}"
                )

    assert mismatches == [], "\n".join(mismatches)
