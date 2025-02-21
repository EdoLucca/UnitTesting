import unittest
from math_utils import MathUtils

class TestMathUtils(unittest.TestCase):
    """

    """


    def test_add(self):
        """
        """
        self.assertEqual(MathUtils.add(1, 2), 3)
        self.assertEqual(MathUtils.add(1.5, 2.5), 4.0)
        self.assertEqual(MathUtils.add(-1, 1), 0)
        self.assertEqual(MathUtils.add(-1.5, 1.5), 0.0)

    def test_subtract(self):
        """
        """
        self.assertEqual(MathUtils.subtract(1, 2), -1)
        self.assertEqual(MathUtils.subtract(1.5, 2.5), -1.0)
        self.assertEqual(MathUtils.subtract(-1, 1), -2)
        self.assertEqual(MathUtils.subtract(-1.5, 1.5), -3.0)

    def test_divide(self):
        """
        """
        self.assertEqual(MathUtils.divide(1, 2), 0.5)
        self.assertEqual(MathUtils.divide(1.5, 2.5), 0.6)
        self.assertEqual(MathUtils.divide(-1, 1), -1)
        self.assertEqual(MathUtils.divide(-1.5, 1.5), -1.0)
        with self.assertRaises(ValueError):
            MathUtils.divide(1, 0)

    def test_multiply(self):
        """
        """
        self.assertEqual(MathUtils.multiply(1, 2), 2)
        self.assertEqual(MathUtils.multiply(10, 2), 20)
        self.assertEqual(MathUtils.multiply(-1, 1), -1)
        self.assertEqual(MathUtils.multiply(-1, 1.5), -1.5)


    def test_power(self):
        """
        """
        self.assertEqual(MathUtils.power(1, 2), 1)
        self.assertEqual(MathUtils.power(2, 2), 4)
        self.assertEqual(MathUtils.power(2.5, 2), 6.25)
        self.assertEqual(MathUtils.power(-1, 2), 1)

    def test_sqrt(self):
        self.assertEqual(MathUtils.power(25, 2), 5)
        self.assertEqual(MathUtils.power(2.5, 2), 1.5)

    def test_absolute(self):
        self.assertEqual(MathUtils.power(1), 1)
        self.assertEqual(MathUtils.power(2.5), 2.5)
        self.assertEqual(MathUtils.power(-2.5), 2.5)
        self.assertEqual(MathUtils.power(-1), 1)