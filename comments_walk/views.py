from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import WalkComment
from .serializers import WalkCommentSerializer, WalkCommentDetailSerializer


class WalkCommentList(generics.ListCreateAPIView):
    """ Walk Comment List view"""
    serializer_class = WalkCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = WalkComment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['walk_post']

    def perform_create(self, serializer):
        """method to create comment"""
        serializer.save(owner=self.request.user)


class WalkCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """Walk Comment Detail view"""
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = WalkCommentDetailSerializer
    queryset = WalkComment.objects.all()

