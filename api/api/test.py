from django.test import TestCase

from api.calc import add 


class CalcTest(TestCase) :
    def test_add_numbers(self):
        """Test 2 numbers adding toghether"""
        self.assertEqual(add(3,8),11)