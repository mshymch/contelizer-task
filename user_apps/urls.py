from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('text/', views.text),
]
