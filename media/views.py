from django.shortcuts import render

from media.models import Image


# Create your views here.

def index(request):
    image = Image.objects.all()
    ctx = {'Image':image}
    return render(request, 'all-media/index.html',ctx)
