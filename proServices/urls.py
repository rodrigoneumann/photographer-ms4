from django.urls import include, path
from .views import services, payment_page, charge, successPage


urlpatterns = [
    path("", services, name="services"),
    path("payment/<str:plan_choice>", payment_page, name="payment_page"),
    path("charge/", charge, name="charge"),
    path("success/<str:plan_type>", successPage, name="success"),
]
