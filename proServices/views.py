from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django.http import JsonResponse
from .models import VideoEditingPlans, UserEditingPlans

import stripe

import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# reading .env file
environ.Env.read_env()

stripe.api_key = env("STRIPE_SECRET_KEY")


def services(request):

    plans = VideoEditingPlans.objects.all()

    return render(request, "services.html", {"plans": plans})


@login_required
def payment_page(request, plan_choice):

    # check if user is already subscribed
    is_subscribed = UserEditingPlans.objects.filter(user=request.user)
    if is_subscribed.exists():
        messages.error(request, "You already have an active video editing plan.")
        return redirect("profile")
    else:
        plan = VideoEditingPlans.objects.filter(type=plan_choice).first()

    return render(request, "services_payment.html", {"plan": plan})


@login_required
def charge(request):

    if request.method == "POST":
        print("Data:", request.POST)

        name = request.user.first_name + ' ' + request.user.last_name
        email = request.user.email
        amount = int(float(request.POST["plan_price"]))
        source = request.POST["stripeToken"]

        plan_type = request.POST["plan_selected"]
        
        customer = stripe.Customer.create(name=name, email=email, source=source)

        stripe.Charge.create(
            customer=customer,
            amount=amount * 100,
            currency="gbp",
            description=plan_type,
        )

    return redirect("success", plan_type=plan_type)


@login_required
def successPage(request, plan_type):

    # Get Stripe payment confirmation and save Subscription information into DB
    plan_selection = VideoEditingPlans.objects.get(type=plan_type)
    newCustomerSub = UserEditingPlans(
        user=request.user,
        editing_plan=plan_selection,
        date_added=timezone.now(),
    )
    newCustomerSub.save()

    return render(request, "success.html")
