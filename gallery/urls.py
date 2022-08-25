from django.urls import path
from gallery import views

urlpatterns = [
    path('gallery-posts/', views.GalleryPostsList.as_view()),
    path('gallery-posts/<int:pk>/', views.GalleryPostDetail.as_view()),
]
