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

# Create your models here.
class Images(models.Model):
    image = CloudinaryField('image')
    name =models.CharField(max_length=20)
    description=models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    
    
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
    def search_by_name(cls,search_term):
        media = cls.objects.filter(name__icontains=search_term)
        return media


