from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Gallery
from .serializers import GallerySerializer


class GalleryPostsList(APIView):
    """Gallery Post List view"""
    serializer_class = GallerySerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        """get method to return all Gallery Posts"""
        gallery_posts = Gallery.objects.all()
        serializer = GallerySerializer(
            gallery_posts, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        """post method to create a Gallery Posts"""
        serializer = GallerySerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )