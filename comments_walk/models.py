from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class WalkComment(models.Model):
    """
    Comment model for Walk Posts, related to User and Gallery
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    walk_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        """Order by most recent first"""
        ordering = ['-created_on']

    def __str__(self):
        return self.content
