from django.urls import path
from .views import UserAPIView
urlpatterns = [
    path('login/', UserAPIView.as_view()), #it will give nice format of the api
    path('login/<int:pk>',UserAPIView.as_view()),
]
