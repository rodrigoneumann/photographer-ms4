from django.db import models
from django.conf import settings

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your models here.
PLAN_CHOICES = (
    ("single", "Single Job"),
    ("weekly", "Weekly Plan"),
    ("monthly", "Monthly Plan"),
)


class VideoEditingPlans(models.Model):
    type = models.CharField(max_length=18, choices=PLAN_CHOICES)
    description = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.type


class UserEditingPlans(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    editing_plan = models.ForeignKey(
        VideoEditingPlans, on_delete=models.SET_NULL, null=True
    )
    date_added = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
