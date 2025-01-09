import unittest
import hypot

class TestBadHypot(unittest.TestCase):
    def test_hyp(self):
        self.assertEqual(hypot.hyp(3, 4), 5)
        self.assertAlmostEqual(hypot.hyp(0, 0), 0.0)

if __name__ == '__main__':
    unittest.main()