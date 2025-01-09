import unittest
from hypot import hyp

class TestHypot(unittest.TestCase):
    """
    Upgraded test suite for the 'hyp' function from 'hypot.py'.
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

    def test_type_error(self):
        """Test that passing non-numeric values raises TypeError."""
        with self.assertRaises(TypeError):
            hyp("three", "four")

if __name__ == '__main__':  # pragma: no cover
    unittest.main()          # pragma: no cover
