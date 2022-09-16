from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from location_field.models.plain import PlainLocationField


class Profile(models.Model):
    """Model for Profile"""
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=150, blank=True)
    location = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_hkhita'
    )

    class Meta:
        """Order by most recent first"""
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    """Function to create a profile every time a user is created"""
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
