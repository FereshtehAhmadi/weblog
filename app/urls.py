from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('', views.login, name= 'login'),
    path('signup/', views.register, name= 'register'),
    path('home/<str:user>', views.home, name= 'home'),
    path('add/', views.add_post, name= 'add'),
]