from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """Model for Walk Post"""

    environment_choices = [
        ('coastal', 'Coastal'),
        ('woodland', 'Woodland'),
        ('countryside', 'Countryside'),
        ('moorland', 'Moorland'),
        ('hill', 'Hill'),
        ('mountain', 'Mountain'),
        ('peak', 'Peak'),
        ('city', 'City'),
        ('other', 'Other'),
    ]

    wc_choices = [
        ('yes', 'Yes'),
        ('no', 'No'),
        ('unknown', 'Unknown'),
        
    ]

    dog_friendly = [
        ('yes', 'Yes'),
        ('no', 'No'),
        ('unknown', 'Unknown'),
    ]

    difficulty = [
        ('easy', 'Easy'),
        ('moderate', 'Moderate'),
        ('challenging', 'Challenging'),
        ('unknown', 'Unknown'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    headline = models.CharField(max_length=500)
    image = models.ImageField(
        upload_to='images/', default='../default_post_e14ubs.jpg', blank=True
    )
    environment = models.CharField(
        max_length=55,
        choices=environment_choices,
        default='other',
    )
    wc = models.CharField(
        max_length=20,
        choices=wc_choices,
        default='unknown',
    )
    dog_friendly = models.CharField(
        max_length=20,
        choices=dog_friendly,
        default='unknown',
    )
    difficulty = models.CharField(
        max_length=55,
        choices=difficulty,
        default='unknown',
    )
    length = models.CharField(max_length=55)
    duration = models.CharField(max_length=55)
    content = models.TextField(blank=True)

    class Meta:
        """Order by most recent first"""
        ordering = ['-updated_on']

    def __str__(self):
        return f'{self.id} {self.title}'
