# from django.http import Http404
# from rest_framework import status, permissions
# from rest_framework.views import APIView
# from rest_framework.response import Response
from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer

class WalkPostsList(generics.ListCreateAPIView):
    """List walk posts or create walk post if logged in"""
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        walk_save_count=Count('saved', distinct=True),
        walk_comments_count=Count('walkcomment', distinct=True)
    ).order_by('-updated_on')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    search_fields = [
        'owner__username',
        'title',
        'environment',
        'difficulty',
    ]
    filterset_fields = [
        'owner__followed__owner__profile',
        'saved__owner__profile',
        'owner__profile',
    ]
    ordering_fields = [
        'walk_save_count',
        'walk_comments_count',
        'walked_saved__updated_on',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class WalkPostDetail(generics.RetrieveUpdateDestroyAPIView):
    """Allows walk post owner to retrieve, update or delete their own post"""
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        walk_save_count=Count('saved', distinct=True),
        walk_comments_count=Count('walkcomment', distinct=True)
    ).order_by('-updated_on')
