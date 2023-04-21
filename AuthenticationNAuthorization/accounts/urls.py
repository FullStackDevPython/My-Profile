from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.get_all_user, name='get_users'),
    path('create-user/', views.register, name='Create_user')
] 
