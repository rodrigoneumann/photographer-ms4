from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class RegisterForm(UserCreationForm):
    """ Form to register a new user """
    first_name = forms.CharField(max_length=15, required=True)
    last_name = forms.CharField( max_length=30, required=True)
    email = forms.EmailField(min_length=3, max_length=45, required=True)
    username = forms.CharField(
        min_length=4,
        max_length=15,
        required=True,
        help_text="Your username must contain at least 4 characters.",
    )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "username",
            "password1",
            "password2",
        ]

class EditProfileForm(UserChangeForm):
    """ Form to edit user name and email, exclude password """
    password = None

    #User profile fields to display
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
        ]
        
