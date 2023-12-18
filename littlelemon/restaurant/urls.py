from django.contrib import admin
from django.urls import path
from . import views
from .views import sayHello

urlpatterns = [
    path('', views.index, name='index'),
    path('', sayHello, name='sayHello'),
]