from django.db import models
from django.contrib.auth.models import User


class Gallery(models.Model):
    """Model for Gallery Post"""
    category_choices = [
        ('photography', 'Photography'),
        ('artwork', 'Artwork'),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    category = models.CharField(
        max_length=55,
        choices=category_choices,
        default=0
    )
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_e14ubs.jpg', blank=True
    )

    class Meta:
        """Order by most recent first"""
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.title}'
