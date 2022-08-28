from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import WalkComment
from .serializers import WalkCommentSerializer, WalkCommentDetailSerializer


class WalkCommentList(generics.ListCreateAPIView):
    """ Walk Comment List view"""
    serializer_class = WalkCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = WalkComment.objects.all()

    def perform_create(self, serializer):
        """method to create comment"""
        serializer.save(owner=self.request.user)


class WalkCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """Walk Comment Detail view"""
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = WalkCommentDetailSerializer
    queryset = WalkComment.objects.all()

