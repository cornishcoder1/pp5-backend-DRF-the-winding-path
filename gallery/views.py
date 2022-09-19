from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Gallery
from .serializers import GallerySerializer

class GalleryPostsList(generics.ListCreateAPIView):
    """List gallery posts or create gallery post if logged in"""
    serializer_class = GallerySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Gallery.objects.annotate(
        gallery_likes_count=Count('likes', distinct=True),
        gallery_comments_count=Count('gallerycomment', distinct=True)
    ).order_by('-updated_on')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    search_fields = [
        'owner__username',
        'title',
    ]
    filterset_fields = [
        'owner__followed__owner__profile',
        'likes__owner__profile',
        'owner__profile',
    ]
    ordering_fields = [
        'gallery_likes_count',
        'gallery_comments_count',
        'gallery_likes__created_on',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class GalleryPostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Allows gallery post owner to retrieve, update or delete their own post
    """
    serializer_class = GallerySerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Gallery.objects.annotate(
        gallery_likes_count=Count('likes', distinct=True),
        gallery_comments_count=Count('gallerycomment', distinct=True)
    ).order_by('-updated_on')
