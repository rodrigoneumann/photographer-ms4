from django.contrib.auth import views as auth_views
from django.urls import include, path
from .views import register, profile, edit_profile, delete_user
from accounts import urls_pwd_rst


urlpatterns = [
    path("register/", register, name="register"),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="login.html", redirect_authenticated_user=True
        ),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="logout.html"),
        name="logout",
    ),
    path("profile/", profile, name="profile"),
    path("profile/edit", edit_profile, name="edit_profile"),
    path("pwd-reset/", include(urls_pwd_rst)),
    path("delete-user/", delete_user, name="delete_user"),
]
