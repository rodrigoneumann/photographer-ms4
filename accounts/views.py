from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from proServices.models import UserEditingPlans, VideoEditingPlans
from .forms import RegisterForm, EditProfileForm


def register(request):
    # check if user is autthenticated
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
    
    #check if user is authentited  
    if request.user.is_authenticated is False:
        messages.error(
            request, "You are not authenticated, please login to view this page"
        )
        return redirect("login")
    
    # check subscription
    is_subscribed = UserEditingPlans.objects.filter(user=request.user).first()
    if is_subscribed != None:
        subscription = is_subscribed.editing_plan
        plan = VideoEditingPlans.objects.get(type=subscription)
        return render(
            request, "profile.html", {"subscription": subscription, "plan": plan}
        )

    return render(request, "profile.html")


@login_required
def edit_profile(request):
    
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, "edit_profile.html", {"form": form})
