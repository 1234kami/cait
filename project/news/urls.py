from django.urls import path
from .views import *

urlpatterns = [
    path('news/',  NewsListCreateAPIView.as_view())
]