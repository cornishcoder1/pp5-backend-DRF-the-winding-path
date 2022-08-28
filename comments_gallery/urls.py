from django.urls import path
from comments_gallery import views

urlpatterns = [
    path('comments_gallery/', views.GalleryCommentList.as_view()),
    path('comments_gallery/<int:pk>/', views.GalleryCommentDetail.as_view()),
]
