from django.urls import path
from comments_walk import views

urlpatterns = [
    path('comments-walk/', views.WalkCommentList.as_view()),
    path('comments-walk/<int:pk>/', views.WalkCommentDetail.as_view()),
]
