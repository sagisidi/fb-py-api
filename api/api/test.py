from django.test import SimpleTestCase

from api import calc


class CalcTest(SimpleTestCase):
    def test_add_numbers(self):
        """Test 2 numbers adding toghether"""
        self.assertEqual(calc.add(3, 8), 11)

    def test_sub_numbers(self):
        """Test subtruct 2 number"""
        self.assertEqual(calc.subtruct(8, 3), 5)
