from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class WalkPostDetailViewTests(APITestCase):
    """Walk Post Detail View Tests"""
    def setUp(self):
        paul = User.objects.create_user(username='paul', password='pass')
        jane = User.objects.create_user(username='jane', password='pass')
        Post.objects.create(
            owner=paul, title='a title', content='pauls content',
            length='1 mile', duration='1 hour', headline='test headline',
        )
        Post.objects.create(
            owner=jane, title='another title', content='janes content',
            length='1 mile', duration='1 hour', headline='test headline',
        )

    def test_can_retrieve_post_using_valid_id(self):
        """Test that a user can retrieve a post using a valid ID"""
        response = self.client.get('/walk-posts/1/')
        self.assertEqual(response.data['title'], 'a title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_post_using_invalid_id(self):
        """Test that a user can't retrieve a post using an invalid ID"""
        response = self.client.get('/walk-posts/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_post(self):
        """Test that a user can update their own post"""
        self.client.login(username='paul', password='pass')
        response = self.client.put('/walk-posts/1/', {
            'title': 'a title', 'length': '2 miles',
            'duration': '1 hour', 'headline': 'test headline',
        })
        walk_post = Post.objects.filter(pk=1).first()
        print(response.data)
        self.assertEqual(walk_post.length, '2 miles')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_post(self):
        """Test that a user can't update another user's post"""
        self.client.login(username='paul', password='pass')
        response = self.client.put('/walk-posts/2/', {
            'title': 'a new title', 'owner': 'paul'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
