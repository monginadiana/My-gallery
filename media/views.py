from django.shortcuts import render
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

from media.models import Images


# Create your views here.


def index(request):
    images = Images.objects.all()
    ctx = {'images':images}
    return render(request, 'all-media/index.html',ctx)

def search_results(request):

    if 'images' in request.GET and request.GET["images"]:
        search_term = request.GET.get("images")
        searched_images = Images.search_by_category(search_term)
        message = search_term

        return render(request, 'all-media/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-media/search.html',{"message":message})
def image(request,image_id):
    try:
        image = Images.objects.get(id = image_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"all-media/image.html", {"image":image})