from django.db import models
from cloudinary.models import CloudinaryField

# category model
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
     #save category to database
    def save_category(self):
        self.save()
    
    # update category to database
    def update_category(self, name):
        self.name = name
        self.save()
        
    # delete category to database
    def delete_category(self):
        self.delete()
    def __str__(self):
        return self.name
    
class Location(models.Model):
    name = models.CharField(max_length = 30)
    
    def save_location(self):
        self.save()

    
    def __str__(self):
        return self.name

# Create your models here.
class Images(models.Model):
    image = CloudinaryField('image')
    name =models.CharField(max_length=20)
    description=models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,null=True)
    
    
    
    
    def save_image(self):
        self.save()
    
    def update_image(self, name, description, category):
        self.name = name
        self.description = description
        self.category = category
        self.save()
    
    # delete image from database
    def delete_image(self):
        self.delete()
    
    def __str__(self):
        return self.name
    
    @classmethod
    def filter_by_category(cls,search_term):
        images = cls.objects.filter(category__name__icontains=search_term)
        return images
    
    @classmethod
    def filter_by_location(cls,search_location):
        images = cls.objects.filter(location__name__icontains=search_location).all()
        return images

    @classmethod
    def search(cls, search_term):
        images_by_category = cls.filter_by_category(search_term)
        images_by_location = cls.filter_by_location(search_term)
        return images_by_category.union(images_by_location)

