from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_home)  # https://localhost:8000/api
]
