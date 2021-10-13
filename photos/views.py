# from typing_extensions import runtime
from django.core.checks import messages
from django.shortcuts import render
from .models import photos,category,location

# Create your views here.
def index(request):
    photo = photos.objects.all()
    ctx = {'photo':photo}
    return render(request, 'index.html',ctx)

def location(request,location):
    location = photos.filterphotosByLocation(location)
    return render(request,'location.html',{'location':location})

def search_results(request):
    if 'category' in request.GET and request.GET["CATEGORY"]:
        search_term = request.GET.get('category')
        seached_photo  = photos.searchphoto(search_term)
        message = f'{search_term}'

        return render(request, 'search.html', {"message":message})
    
    else:
        message = 'you have not serached for any term'
        return render(request, 'search.html',{'message':message})

