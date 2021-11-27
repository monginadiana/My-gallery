from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import  Category, Images, Location

admin.site.register(Images)
admin.site.register(Category)
admin.site.register(Location)
