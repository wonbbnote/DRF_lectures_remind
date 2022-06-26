from django.contrib import admin
from django.urls import path, include
from product import views

urlpatterns = [
    path('product/', views.ProductView.as_view()),
    path("product/<product_id>", views.ProductView.as_view()),
]