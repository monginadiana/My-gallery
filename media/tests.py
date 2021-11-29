from django.test import TestCase
from .models import  Category, Location, Images

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
    
    # image model tests
class ImagesTestCase(TestCase):

    def setUp(self):
        """
        Create a image for testing
        """
        Images.objects.create(
            name="Test Image",
            description="Test Description",
            location=Location.objects.create(name="Image Location"),
            category=Category.objects.create(name="Image Category"),
            
        )
    def test_images_name(self):
        """
        Test that the image name is correct
        """
        image = Images.objects.get(name="Test Image")
        self.assertEqual(image.name, "Test Image")
    
    def test_images_description(self):
        """
        Test that the image description is correct
        """
        image = Images.objects.get(name="Test Image")
        self.assertEqual(image.description, "Test Description")

    def test_images_location(self):
        """
        Test that the image location is correct
        """
        image = Images.objects.get(name="Test Image")
        self.assertEqual(image.location.name, "Image Location")
    
    def test_images_category(self):
        """
        Test that the image category is correct
        """
        image = Images.objects.get(name="Test Image")
        self.assertEqual(image.category.name, "Image Category")
    
    def test_images_str(self):
        """
        Test that the image string representation is correct
        """
        image = Images.objects.get(name="Test Image")
        self.assertEqual(str(image), "Test Image")


    
   


