from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactMeForm
from django.views.defaults import page_not_found


def index(request):
    return render(request, "index.html")


def contact(request):
    """ Contact Form, check if authenticated and auto-fill Name and email
    If POST, get form information provided and Send an e-mail to website contact
    Shows a success message Alert after send
    """
    if request.method == "POST":
        contact_form = ContactMeForm(request.POST)
        if contact_form.is_valid():
            name = request.POST["name"]
            email = request.POST["email"]
            subject = request.POST["subject"]
            message = request.POST["message"]
            send_mail(
                subject,
                "From: " + name + "\n\nEmail: " + email + "\n\nMessage: " + message,
                email,
                ["rodrigoneumann@gmail.com"],
                fail_silently=False,
            )
            messages.success(
                request, "Your message was sent successfully, many Thanks!"
            )
            return redirect("contact")
    else:
        if request.user.is_authenticated:
            contact_form = ContactMeForm(
                initial={
                    "email": request.user.email,
                    "name": request.user.get_full_name,
                }
            )
        else:
            contact_form = ContactMeForm()

    return render(request, "contact.html", {"form": contact_form})


def about(request):
    return render(request, "about.html")
