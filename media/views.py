from django.shortcuts import render

from media.models import Images


# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def index(request):
    Image = Images.objects.all()
    ctx = {'Image':Image}
    return render(request, 'all-media/index.html',ctx)
