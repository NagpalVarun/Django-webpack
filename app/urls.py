from django.contrib import admin
from django.urls import path
from app.views import HomeView
from . import views

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('example/',views.example,name='example'),
]