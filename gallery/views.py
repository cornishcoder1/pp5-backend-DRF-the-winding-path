# from django.http import Http404
# from rest_framework import status, permissions
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.db.models import Count
from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Gallery
from .serializers import GallerySerializer


# class GalleryPostsList(APIView):
#     """Gallery Post List view"""
#     serializer_class = GallerySerializer
#     permission_classes = [
#         permissions.IsAuthenticatedOrReadOnly
#     ]

#     def get(self, request):
#         """get method to return all Gallery Posts"""
#         gallery_posts = Gallery.objects.all()
#         serializer = GallerySerializer(
#             gallery_posts, many=True, context={'request': request}
#         )
#         return Response(serializer.data)

#     def post(self, request):
#         """post method to create a Gallery Post"""
#         serializer = GallerySerializer(
#             data=request.data, context={'request': request}
#         )
#         if serializer.is_valid():
#             serializer.save(owner=request.user)
#             return Response(
#                 serializer.data, status=status.HTTP_201_CREATED
#             )
#         return Response(
#             serializer.errors, status=status.HTTP_400_BAD_REQUEST
#         )

class GalleryPostsList(generics.ListCreateAPIView):
    """List gallery posts or create gallery post if logged in"""
    serializer_class = GallerySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Gallery.objects.annotate(
        gallery_likes_count=Count('likes', distinct=True),
        gallery_comments_count=Count('gallerycomment', distinct=True)
    ).order_by('-created_on')
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


# class GalleryPostDetail(APIView):
#     """Gallery Post Detail view"""
#     serializer_class = GallerySerializer
#     permission_classes = [IsOwnerOrReadOnly]

#     def get_object(self, pk):
#         """Method to handle requests made for a
#         gallery post which does not exist"""
#         try:
#             gallery_post = Gallery.objects.get(pk=pk)
#             self.check_object_permissions(self.request, gallery_post)
#             return gallery_post
#         except Gallery.DoesNotExist:
#             raise Http404

#     def get(self, request, pk):
#         """Get method to return a single Gallery Post instance"""
#         gallery_post = self.get_object(pk)
#         serializer = GallerySerializer(
#             gallery_post,
#             context={'request': request}
#         )
#         return Response(serializer.data)

#     def put(self, request, pk):
#         """Put method to update a Gallery Post instance"""
#         gallery_post = self.get_object(pk)
#         serializer = GallerySerializer(
#             gallery_post, data=request.data,
#             context={'request': request}
#         )
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,
#         status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         """Delete method to delete a Gallery Post instance"""
#         gallery_post = self.get_object(pk)
#         gallery_post.delete()
#         return Response(
#             status=status.HTTP_204_NO_CONTENT
#         )

class GalleryPostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Allows gallery post owner to retrieve, update or delete their own post
    """
    serializer_class = GallerySerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Gallery.objects.annotate(
        gallery_likes_count=Count('likes', distinct=True),
        gallery_comments_count=Count('gallerycomment', distinct=True)
    ).order_by('-created_on')
