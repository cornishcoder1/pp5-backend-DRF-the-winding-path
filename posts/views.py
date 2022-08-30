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


# class WalkPostsList(APIView):
#     """Walk Post List view"""
#     serializer_class = PostSerializer
#     permission_classes = [
#         permissions.IsAuthenticatedOrReadOnly
#     ]

#     def get(self, request):
#         """get method to return all Walk Posts"""
#         walk_posts = Post.objects.all()
#         serializer = PostSerializer(
#             walk_posts, many=True, context={'request': request}
#         )
#         return Response(serializer.data)

#     def post(self, request):
#         """post method to create a Walk Post"""
#         serializer = PostSerializer(
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

class WalkPostsList(generics.ListCreateAPIView):
    """List walk posts or create walk post if logged in"""
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        walk_save_count=Count('saved', distinct=True),
        walk_comments_count=Count('walkcomment', distinct=True)
    ).order_by('-created_on')
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
        'walked_saved__created_on',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# class WalkPostDetail(APIView):
#     """Walk Post Detail view"""
#     serializer_class = PostSerializer
#     permission_classes = [IsOwnerOrReadOnly]

#     def get_object(self, pk):
#         """Method to handle requests made for a
#         walk post which does not exist"""
#         try:
#             walk_post = Post.objects.get(pk=pk)
#             self.check_object_permissions(self.request, walk_post)
#             return walk_post
#         except Post.DoesNotExist:
#             raise Http404

#     def get(self, request, pk):
#         """Get method to return a single Walk Post instance"""
#         walk_post = self.get_object(pk)
#         serializer = PostSerializer(
#             walk_post,
#             context={'request': request}
#         )
#         return Response(serializer.data)

#     def put(self, request, pk):
#         """Put method to update a Walk Post instance"""
#         walk_post = self.get_object(pk)
#         serializer = PostSerializer(
#             walk_post, data=request.data,
#             context={'request': request}
#         )
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         """Delete method to delete a Walk Post instance"""
#         walk_post = self.get_object(pk)
#         walk_post.delete()
#         return Response(
#             status=status.HTTP_204_NO_CONTENT
#         )

class WalkPostDetail(generics.RetrieveUpdateDestroyAPIView):
    """Allows walk post owner to retrieve, update or delete their own post"""
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        walk_save_count=Count('saved', distinct=True),
        walk_comments_count=Count('walkcomment', distinct=True)
    ).order_by('-created_on')


