from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """Profile List view"""
    queryset = Profile.objects.annotate(
        walk_posts_count=Count('owner__post', distinct=True),
        gallery_posts_count=Count('owner__gallery', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True),
    ).order_by('-created_on')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__following__followed__profile',
        'owner__followed__owner__profile',
    ]
    ordering_fields = [
        'walk_posts_count',
        'gallery_posts_count',
        'followers_count',
        'following_count',
        'owner__following__created_on',
        'owner__followed__created_on',
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """Allows profile owner to retrieve and update their own profile"""
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        walk_posts_count=Count('owner__post', distinct=True),
        gallery_posts_count=Count('owner__gallery', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True),
    ).order_by('-created_on')
    serializer_class = ProfileSerializer
