from django.contrib.auth import views as auth_views
from django.urls import include, path
from .views import all_photos


urlpatterns = [
    path("", all_photos, name="photos"),
]