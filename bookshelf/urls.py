from .views import BookAPI
from django.urls import path

urlpatterns = [
    path('', BookAPI.as_view()),
]
