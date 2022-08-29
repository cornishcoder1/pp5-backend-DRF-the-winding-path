from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Save(models.Model):
    """Save model, related to 'owner' and 'walk_post'.
    Users can save a walk post.
    'unique_together' makes sure a user can't save the same post twice."""
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    walk_post = models.ForeignKey(
        Post, related_name='saved', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Order by most recent first"""
        ordering = ['-created_on']
        unique_together = ['owner', 'walk_post']

    def __str__(self):
        return f'{self.owner} {self.walk_post}'
