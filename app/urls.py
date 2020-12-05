from rest_framework import routers
from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views


urlpatterns = [

    path('',views.MovieApi.as_view(), name='movielist'),
    path('movielist/<int:pk>/',views.MovieApi.as_view(), name='update'),
]