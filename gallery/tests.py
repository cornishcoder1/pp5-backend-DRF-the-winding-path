from django.contrib.auth.models import User
from .models import Gallery
from rest_framework import status
from rest_framework.test import APITestCase


class GalleryPostsListViewTests(APITestCase):
    """Gallery Posts List View Test"""
    def setUp(self):
        User.objects.create_user(username='john', password='pass')

    def test_can_list_posts(self):
        """Test that a user can list all Gallery posts"""
        john = User.objects.get(username='john')
        Gallery.objects.create(owner=john, title='a title')
        response = self.client.get('/gallery-posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_post(self):
        """Test that a logged in user can create a post"""
        self.client.login(username='john', password='pass')
        response = self.client.post('/gallery-posts/', {'title': 'a title'})
        count = Gallery.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_cannot_create_post(self):
        """Test that a logged out user cannot create a post"""
        response = self.client.post('/gallery-posts/', {'title': 'a title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

