"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTest(SimpleTestCase):
    """Test and calc module"""

    def test_add_numbers(self):
        """Test adding numbers together"""

        res = calc.add(2, 5)

        self.assertEqual(res, 7)

    def test_subtract_numbers(self):
        """Test subtracting numbers"""

        res = calc.subtract(5, 3)

        self.assertEqual(res, 2)
