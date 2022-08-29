from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from save.models import Save
from save.serializers import SaveSerializer


class SaveList(generics.ListCreateAPIView):
    """Walk Post Save List view"""
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = SaveSerializer
    queryset = Save.objects.all()

    def perform_create(self, serializer):
        """method to create save"""
        serializer.save(owner=self.request.user)


class SaveDetail(generics.RetrieveDestroyAPIView):
    """Walk Post Save Detail view"""
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = SaveSerializer
    queryset = Save.objects.all()

