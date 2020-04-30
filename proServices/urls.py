from django.urls import include, path
from .views import services


urlpatterns = [
    path("", services, name="services"),
]