from django.urls import path
from save import views

urlpatterns = [
    path('save/', views.SaveList.as_view()),
    path('save/<int:pk>/', views.SaveDetail.as_view()),
]
