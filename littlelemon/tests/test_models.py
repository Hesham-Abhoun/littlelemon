from django.test import TestCase
from .models import Menu 

class MenuTest(TestCase):
    
    def test_menu_item_creation(self):
        # Create a new instance of the Menu model
        menu_item = Menu.objects.create(name="Pasta", price=9.99, description="Delicious pasta with marinara sauce",is_available=True)
        
        # Define the expected string representation
        expected_string = "Pasta - $9.99"

        # Assert that the string representation is as expected
        self.assertEqual(str(menu_item), expected_string)
