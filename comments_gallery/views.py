from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import GalleryComment
from .serializers import GalleryCommentSerializer, GalleryCommentDetailSerializer


class GalleryCommentList(generics.ListCreateAPIView):
    """Gallery Comment List view"""
    serializer_class = GalleryCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = GalleryComment.objects.all()

    def perform_create(self, serializer):
        """method to create comment"""
        serializer.save(owner=self.request.user)


class GalleryCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """Gallery Comment Detail view"""
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = GalleryCommentDetailSerializer
    queryset = GalleryComment.objects.all()
