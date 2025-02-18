""" sample tests  """
from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """ test the calc module"""
    def test_add_numbers(self):
        """Test adding numbers together"""
        res= calc.add(5,10)
        self.assertEqual(res, 15)
    def test_subtract_number(self):
        """Test for subtracting numbers"""
        res = calc.subtract(10,8)
        self.assertEqual(res, 2)
            
