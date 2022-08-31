from django.db import models


class Contact(models.Model):
    """Model for Contact Form"""
    fname = models.CharField(max_length=55)
    lname = models.CharField(max_length=55)
    email = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Order by most recent first"""
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.fname} {self.lname}'
