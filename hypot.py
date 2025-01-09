"""
This module provides a function to calculate the hypotenuse using math.hypot.
It includes extensive input checks to ensure all arguments are valid real numbers.
"""

import math


def hyp(x, y):
    """
    Calculate the hypotenuse of a right triangle using math.hypot, with thorough
    validation of inputs.

    :param x: The length of one side (must be a real number).
    :param y: The length of the other side (must be a real number).
    :type x: int or float
    :type y: int or float
    :raises ValueError: If x or y is None, NaN, or infinite.
    :raises TypeError: If x or y is not an int or float.
    :return: The calculated hypotenuse as a float.
    :rtype: float
    """

    # Check for None
    if x is None or y is None:
        raise ValueError("Arguments x and y cannot be None.")

    # Check for correct type
    if not isinstance(x, (int, float)):
        raise TypeError(
            f"Argument x must be int or float, got {type(x).__name__} instead."
        )
    if not isinstance(y, (int, float)):
        raise TypeError(
            f"Argument y must be int or float, got {type(y).__name__} instead."
        )

    # Check for NaN
    if math.isnan(x) or math.isnan(y):
        raise ValueError("Arguments x and y cannot be NaN.")

    # Check for infinite values
    if not math.isfinite(x) or not math.isfinite(y):
        raise ValueError("Arguments x and y cannot be infinite.")

    # If all checks pass, compute the hypotenuse
    return math.hypot(x, y)
