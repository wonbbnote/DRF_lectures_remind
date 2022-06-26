from django.contrib import admin
from django.urls import path, include
from user import views

urlpatterns = [
    path('login/', views.UserApiView.as_view()),
]