from django.db import models
from django.contrib.auth.models import User
from gallery.models import Gallery


class GalleryComment(models.Model):
    """
    Comment model for Gallery Posts, related to User and Gallery
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    gallery_post = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.content
