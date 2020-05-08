from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

class Photo(models.Model):
    CATEGORY_CHOICES = (
    ('Music', 'Music Shows'),
    ('Studio', 'Studio'),
    ('Food', 'Food'),
    ('Weeding', 'Weeding'),
    ('Travel', 'Travel')
    )

    title = models.CharField(max_length=254, default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=20, default='')
    description = models.TextField()
    image = models.FileField()
    
    def __str__(self):
        return self.title

class Video(models.Model):
    CATEGORY_CHOICES = (
    ('institutional', 'Institutional'),
    ('music', 'Music'),
    ('events', 'Events'),
    ('drone', 'Drone'),
    )

    title = models.CharField(max_length=254, default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=20, default='')
    description = models.TextField()
    videoUrl = models.URLField()
    
    def __str__(self):
        return self.title

# Delete image from the server in case of entry deletion
@receiver(post_delete, sender=Photo)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False) 
