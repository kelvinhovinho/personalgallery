# from typing_extensions import runtime
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




