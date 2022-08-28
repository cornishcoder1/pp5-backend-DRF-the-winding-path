from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import GalleryComment
from .serializers import GalleryCommentSerializer, GalleryCommentDetailSerializer


class GalleryCommentList(generics.ListCreateAPIView):
    serializer_class = GalleryCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = GalleryComment.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class GalleryCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = GalleryCommentDetailSerializer
    queryset = GalleryComment.objects.all()
