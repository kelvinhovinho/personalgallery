# from typing_extensions import runtime
from django.shortcuts import render
from .models import photos

# Create your views here.
def index(request):
    photo = photos.objects.all()
    ctx = {'photo':photo}
    return render(request, 'index.html',ctx)

