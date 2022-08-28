from django.urls import path
from comments_walk import views

urlpatterns = [
    path('comments_walk/', views.WalkCommentList.as_view()),
    path('comments_walk/<int:pk>/', views.WalkCommentDetail.as_view()),
]
