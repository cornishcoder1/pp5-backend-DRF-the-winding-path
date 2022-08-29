# from django.contrib.auth.models import User
# from .models import Gallery
# from rest_framework import status
# from rest_framework.test import APITestCase


# class GalleryPostsListViewTests(APITestCase):
#     """Gallery Posts List View Tests"""
#     def setUp(self):
#         User.objects.create_user(username='john', password='pass')

#     def test_can_list_posts(self):
#         """Test that a user can list all Gallery posts"""
#         john = User.objects.get(username='john')
#         Gallery.objects.create(owner=john, title='a title')
#         response = self.client.get('/gallery-posts/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         print(response.data)
#         print(len(response.data))

#     def test_logged_in_user_can_create_post(self):
#         """Test that a logged in user can create a post"""
#         self.client.login(username='john', password='pass')
#         response = self.client.post('/gallery-posts/', {'title': 'a title'})
#         count = Gallery.objects.count()
#         self.assertEqual(count, 1)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#     def test_logged_out_user_cannot_create_post(self):
#         """Test that a logged out user cannot create a post"""
#         response = self.client.post('/gallery-posts/', {'title': 'a title'})
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


# class GalleryPostDetailViewTests(APITestCase):
#     """Gallery Post Detail View Tests"""
#     def setUp(self):
#         john = User.objects.create_user(username='john', password='pass')
#         sarah = User.objects.create_user(username='sarah', password='pass')
#         Gallery.objects.create(
#             owner=john, title='a title', content='johns content'
#         )
#         Gallery.objects.create(
#             owner=sarah, title='another title', content='sarahs content'
#         )

#     def test_can_retrieve_post_using_valid_id(self):
#         """Test that a user can retrieve a post using a valid ID"""
#         response = self.client.get('/gallery-posts/1/')
#         self.assertEqual(response.data['title'], 'a title')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_cant_retrieve_post_using_invalid_id(self):
#         """Test that a user can't retrieve a post using an invalid ID"""
#         response = self.client.get('/gallery-posts/999/')
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

#     def test_user_can_update_own_post(self):
#         """Test that a user can update their own post"""
#         self.client.login(username='john', password='pass')
#         response = self.client.put('/gallery-posts/1/', {
#             'title': 'a new title'
#         })
#         gallery_post = Gallery.objects.filter(pk=1).first()
#         self.assertEqual(gallery_post.title, 'a new title')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_user_cant_update_another_users_post(self):
#         """Test that a user can't update another user's post"""
#         self.client.login(username='john', password='pass')
#         response = self.client.put('/gallery-posts/2/', {
#             'title': 'a new title'
#         })
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

