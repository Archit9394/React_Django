from django.urls import path
from .views import UserAPIView
urlpatterns = [
    path('login/', UserAPIView.as_view()),
    path('login/<int:pk>',UserAPIView.as_view()),
]
