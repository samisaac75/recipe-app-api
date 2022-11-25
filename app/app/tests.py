"""
Sample Tests
"""
from django.test import SimpleTestCase
from app import calc

class CalcTests(SimpleTestCase):
    """Test the calc module""" 

    def test_add_numbers(self):
        """Test Adding Numbers"""
        res = calc.add(10, 20)

        self.assertEqual(res, 30)

    def test_subtract_numbers(self):
        """Testing suntracting numbers"""

        res = calc.subtract(15, 10)

        self.assertEquals(res, -5)