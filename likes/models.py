from django.db import models
from django.contrib.auth.models import User
from gallery.models import Gallery


class Like(models.Model):
    """Like model, related to 'owner' and 'gallery_post'.
    Users can like a gallery post.
    'unique_together' makes sure a user can't like the same post twice."""
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    gallery_post = models.ForeignKey(
        Gallery, related_name='likes', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Order by most recent first"""
        ordering = ['-created_on']
        unique_together = ['owner', 'gallery_post']

    def __str__(self):
        return f'{self.owner} {self.gallery_post}'
