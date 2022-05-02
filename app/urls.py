from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('', views.login, name= 'login'),
    path('signup/', views.register, name= 'register'),
    path('home/', views.home, name= 'home'),
]
