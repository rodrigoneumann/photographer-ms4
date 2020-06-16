from django.urls import include, path
from .views import about, contact


urlpatterns = [
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
]
