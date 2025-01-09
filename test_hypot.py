"""
Unit tests for the `hyp` function from the `hypot` module.
It covers all input checks.
"""

import math
import unittest

from hypot import hyp


class TestGoodHypot(unittest.TestCase):
    """
    Thorough test suite for the 'hyp' function from 'hypot.py'.
    """

    def test_positive_values(self):
        """Test standard positive integers."""
        self.assertEqual(hyp(3, 4), 5)

    def test_zero_values(self):
        """Test zero input results in 0.0."""
        self.assertEqual(hyp(0, 0), 0.0)

    def test_negative_values(self):
        """Test negative inputs yield a positive distance."""
        self.assertAlmostEqual(hyp(-3, -4), 5)

    def test_float_values(self):
        """Test floating-point inputs with approximate comparison."""
        self.assertAlmostEqual(hyp(3.5, 4.5), 5.70087712549569)

    def test_none_input(self):
        """Test that None input raises ValueError."""
        with self.assertRaises(ValueError):
            hyp(None, 4)
        with self.assertRaises(ValueError):
            hyp(3, None)

    def test_nan_input(self):
        """Test that NaN input raises ValueError."""
        with self.assertRaises(ValueError):
            hyp(math.nan, 4)
        with self.assertRaises(ValueError):
            hyp(3, math.nan)

    def test_infinite_input(self):
        """Test that infinite values raise ValueError."""
        with self.assertRaises(ValueError):
            hyp(math.inf, 4)
        with self.assertRaises(ValueError):
            hyp(3, -math.inf)

    def test_non_numeric_input(self):
        """Test that non-numeric values raise TypeError."""
        with self.assertRaises(TypeError):
            hyp("three", 4)
        with self.assertRaises(TypeError):
            hyp(3, [4])

    def test_type_error(self):
        """
        Example test that passing non-numeric values raises TypeError.
        Separated for clarity.
        """
        with self.assertRaises(TypeError):
            hyp("three", "four")


if __name__ == '__main__':  # pragma: no cover
    unittest.main()          # pragma: no cover
