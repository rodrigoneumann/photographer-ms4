from django.shortcuts import render
from .models import Photo, Video


def portfolio(request):
    return render(request, "portfolio.html")

#Photo Gallery Views
def all_photos(request):
    photos = Photo.objects.all()
    return render(request, "photo.html", {"photos": photos})


def music_view(request):
    photos = Photo.objects.filter(category="Music")
    category_name = "Music Shows"
    return render(
        request, "photo.html", {"photos": photos, "category": category_name}
    )


def studio_view(request):
    photos = Photo.objects.filter(category="Studio")
    category_name = "Studio"
    return render(
        request, "photo.html", {"photos": photos, "category": category_name}
    )


def food_view(request):
    photos = Photo.objects.filter(category="Food")
    category_name = "Food"
    return render(
        request, "photo.html", {"photos": photos, "category": category_name}
    )


def weeding_view(request):
    photos = Photo.objects.filter(category="Weeding")
    category_name = "Weeding"
    return render(
        request, "photo.html", {"photos": photos, "category": category_name}
    )


def drone_view(request):
    photos = Photo.objects.filter(category="Drone")
    category_name = "Drone"
    return render(
        request, "photo.html", {"photos": photos, "category": category_name}
    )

def fineArt_view(request):
    photos = Photo.objects.filter(category="FineArt")
    category_name = "Fine Art"
    return render(
        request, "photo.html", {"photos": photos, "category": category_name}
    )


#Video gallery Views

def all_videos(request):
    videos = Video.objects.all()
    return render(request, "video.html", {"videos": videos})


def institutional_videos_view(request):
    videos = Video.objects.filter(category="institutional")
    category_name = "Institutional"
    return render(
        request, "video.html", {"videos": videos, "category": category_name}
    )

def shows_videos_view(request):
    videos = Video.objects.filter(category="videoMusic")
    category_name = "Music"
    return render(
        request, "video.html", {"videos": videos, "category": category_name}
    )

def events_videos_view(request):
    videos = Video.objects.filter(category="events")
    category_name = "Events"
    return render(
        request, "video.html", {"videos": videos, "category": category_name}
    )

def drone_videos_view(request):
    videos = Video.objects.filter(category="drone")
    category_name = "Drone"
    return render(
        request, "video.html", {"videos": videos, "category": category_name}
    )
