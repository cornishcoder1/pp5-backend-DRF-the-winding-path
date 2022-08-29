# from django.http import Http404
# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from drf_api.permissions import IsOwnerOrReadOnly
from rest_framework import generics
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


# class ProfileList(APIView):
#     """Profile List view"""
#     def get(self, request):
#         """get method to return all Profiles"""
#         profiles = Profile.objects.all()
#         serializer = ProfileSerializer(profiles, many=True,
#         context={'request': request})
#         return Response(serializer.data)

class ProfileList(generics.ListAPIView):
    """Profile List view"""
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


# class ProfileDetail(APIView):
#     """Profile Detail view"""
#     serializer_class = ProfileSerializer
#     permission_classes = [IsOwnerOrReadOnly]

#     def get_object(self, pk):
#         """Method to handle requests made for a profile which does not exist"""
#         try:
#             profile = Profile.objects.get(pk=pk)
#             self.check_object_permissions(self.request, profile)
#             return profile
#         except Profile.DoesNotExist:
#             raise Http404

#     def get(self, request, pk):
#         """Get method to return a single Profile instance"""
#         profile = self.get_object(pk)
#         serializer = ProfileSerializer(profile, context={'request': request})
#         return Response(serializer.data)

#     def put(self, request, pk):
#         """Put method to update a Profile instance"""
#         profile = self.get_object(pk)
#         serializer = ProfileSerializer(profile, data=request.data, context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileDetail(generics.RetrieveUpdateAPIView):
    """Allows profile owner to retrieve and update their own profile"""
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
