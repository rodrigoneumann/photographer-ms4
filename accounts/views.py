from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils import timezone
from proServices.models import UserEditingPlans, VideoEditingPlans
from .forms import RegisterForm, EditProfileForm


def register(request):
    """ Renders the registration page """
    if request.user.is_authenticated:
        return redirect(reverse("index"))

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})


@login_required
def profile(request):
    """ Renders the user's profile page with info about personal details
    and subscription plan details, if subscribed. """

    if request.user.is_authenticated is False:
        messages.error(
            request, "You are not authenticated, please login to view this page"
        )
        return redirect("login")

    # check subscription
    is_subscribed = UserEditingPlans.objects.filter(user=request.user).first()
    if is_subscribed != None:

        subscription = is_subscribed.editing_plan
        plan = str(VideoEditingPlans.objects.get(type=subscription))
        status = is_subscribed.is_active

        if plan == "Weekly Plan":
            date_added = is_subscribed.date_added
            end = date_added + timezone.timedelta(days=7)
            daysRemaining = (end - timezone.now()).days
            if daysRemaining == 0:
                subscription = None
            else:
                end = str(end.date())
                status = "Your subscription is valid until : " + end

        if plan == "Monthly Plan":
            date_added = is_subscribed.date_added
            end = date_added + timezone.timedelta(days=30)
            daysRemaining = (end - timezone.now()).days
            if daysRemaining == 0:
                subscription = None
            else:
                end = str(end.date())
                status = "Your subscription is valid until : " + end

        return render(
            request,
            "profile.html",
            {"subscription": subscription, "plan": plan, "status": status},
        )

    return render(request, "profile.html")


@login_required
def edit_profile(request):
    """ Renders update page for the user. """
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, "edit_profile.html", {"form": form})


@login_required
def delete_user(request):
    """ Renders delete user confirmation page, check if user is subscribed
    if there's a subscription active, it should be not possible to delete """
    user = User.objects.get(id=request.user.id)
    is_subscribed = UserEditingPlans.objects.filter(user=user).first()

    if is_subscribed == None:
        if request.method == "POST":
            user.delete()
            return redirect("index")
        return render(request, "delete_confirm.html")
    messages.error(
        request, "It is not possible to delete the user with an active subscription."
    )
    return redirect("profile")
