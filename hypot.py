"""
This module provides a function to calculate the hypotenuse using math.hypot.
"""

import math


def hyp(x, y):
    """
    Calculate the hypotenuse of a right triangle using the built-in math.hypot.

    :param x: The length of one side
    :param y: The length of the other side
    :return: The calculated hypotenuse as a float
    """
    return math.hypot(x, y)
