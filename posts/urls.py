from django.urls import path
from posts import views

urlpatterns = [
    path('walk-posts/', views.WalkPostsList.as_view()),
    path('walk-posts/<int:pk>/', views.WalkPostDetail.as_view()),
]
