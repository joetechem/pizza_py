import unittest
from pizza import make_pizza

class PizzaTestCase(unittest.TestCase):
    """Tests for 'pizza.py'."""

    def test_size_topping(self):
        """Do any size pizzas with one topping work?"""
        formatted_name = get_formatted_name('jimi', 'hendrix')
        self.assertEqual(formatted_name, 'Jimi Hendrix')


unittest.main()

