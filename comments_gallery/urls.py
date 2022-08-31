from django.urls import path
from comments_gallery import views

urlpatterns = [
    path('comments-gallery/', views.GalleryCommentList.as_view()),
    path('comments-gallery/<int:pk>/', views.GalleryCommentDetail.as_view()),
]
