from django.shortcuts import render
from .models import Photo

def all_photos(request):
    photos = Photo.objects.all()
    return render(request, "portfolio.html", {"photos": photos})

