from django.test import TestCase
from .models import  Category, Location

# Create your tests here.

# category models test
class CategoryTestCase(TestCase):

    def setUp(self):
        """
        Create a category for testing
        """
        Category.objects.create(name="Image Category")
        
    def test_category_name(self):
        """
        Test that the category name is correct
        """
        category = Category.objects.get(name="Image Category")
        self.assertEqual(category.name, "Image Category")

    def test_category_str(self):
        """
        Test that the category string representation is correct
        """
        category = Category.objects.get(name="Image Category")
        self.assertEqual(str(category), "Image Category")

# location model tests
class LocationTestCase(TestCase):

    def setUp(self):
        """
        Create a setup for testing locaation
        """
        Location.objects.create(name="Image Location")
    
    def test_location_name(self):
        """
        Test that the location name is correct
        """
        location = Location.objects.get(name="Image Location")
        self.assertEqual(location.name, "Image Location")
        
    def test_location_str(self):
        """
        Test that the location string representation is correct
        """
        location = Location.objects.get(name="Image Location")
        self.assertEqual(str(location), "Image Location")
    
   


