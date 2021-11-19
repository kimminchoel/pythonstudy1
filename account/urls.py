from django import VERSION
from django.urls import path
from . import views

urlpatterns = [

    path('', views.main, name = 'main'),
    path('sign/', views.sign, name = 'sign'),
    path('logout/', views.logout, name = 'logout')
]