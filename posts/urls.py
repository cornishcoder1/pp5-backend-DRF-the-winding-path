from django.urls import path
from posts import views

urlpatterns = [
    path('walk-posts/', views.WalkPostsList.as_view()),
]
