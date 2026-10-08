# Triangle Classifier

`triangle.py` provides two functions:

- `is_valid_triangle(a, b, c) -> bool`: returns `True` only if all three sides are positive and they pass the strict triangle inequality. A degenerate triangle, where two sides add up to exactly the third, is invalid.
- `classify_triangle(a, b, c) -> str`: returns `"Invalid"`, `"Equilateral"`, `"Isosceles"` or `"Scalene"`. If the sides also satisfy the Pythagorean theorem, the result starts with `"Right "`, for example `"Right Scalene"` or `"Right Isosceles"`.

The right-triangle check uses `math.isclose` with a relative tolerance instead of `==`. This means floating-point inputs such as `(1, 1, math.sqrt(2))` are still classified as `"Right Isosceles"`.

## Usage

```python
from triangle import classify_triangle

classify_triangle(3, 4, 5)   # "Right Scalene"
classify_triangle(2, 2, 3)   # "Isosceles"
classify_triangle(1, 2, 3)   # "Invalid" (degenerate)
```

## Why an equilateral triangle can never be right

Every angle in an equilateral triangle is 60°, so none of them can be 90°. In terms of the sides, a right triangle needs a² + a² = a², which simplifies to 2a² = a² and only holds when a = 0. A side of 0 is not a valid triangle.

## Copilot Review Log


| Test | What it checks | Copilot suggestion | Kept / edited / rejected | Why |
| --- | --- | --- | --- | --- |
| `test_triangle_classification` | One case each for Equilateral `(4,4,4)`, Isosceles `(2,2,3)`, Scalene `(4,5,6)`, Right Scalene `(3,4,5)` and Invalid `(0,2,2)` | No suggestion received | Not applicable | Checked each expected label against the documented classification rules. |
| `test_degenerate_triangle_is_invalid` | `(1,2,3)`, where two sides add up exactly to the third, is invalid in both functions | No suggestion received | Not applicable | Confirmed the strict triangle inequality makes a degenerate triangle invalid. |
| `test_negative_side_is_invalid` | `(-1,2,2)` is invalid in both functions because every side must be positive | No suggestion received | Not applicable | Reviewed against the positive-side requirement; zero is not the only non-positive invalid input. Passes. The negative's position doesn't matter because the triangle inequality also fails whenever any side is ≤ 0, so one position is enough. |
| `test_right_isosceles_with_non_integer_hypotenuse` | `(5, 5, 5√2)` is `"Right Isosceles"` | No suggestion received | Not applicable; equality pitfall caught in review | An exact `==` check is unsuitable for this floating-point Pythagorean calculation; the spec requires tolerance-based recognition. This was a manual review finding, not a Copilot suggestion. |
| `test_equilateral_triangle_is_not_right` | `(5,5,5)` is plain `"Equilateral"`, never Right | No suggestion received | Not applicable | Checked that the expected result follows the documented right-triangle rule and that equilateral triangles are not right. |
