import math

def hyp(x: float, y: float) -> float:
    """
    Calculate the hypotenuse of a right triangle using math.hypot(x, y).
    
    :param x: Length of one side
    :param y: Length of the other side
    :return: Hypotenuse as a float
    """
    return math.hypot(x, y)
