from django.contrib import admin
from .models import VideoEditingPlans, UserEditingPlans

# Register your models here.

admin.site.register(VideoEditingPlans)
admin.site.register(UserEditingPlans)