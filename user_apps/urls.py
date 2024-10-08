from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('text/', views.upload_file),
    path('display/', views.display_file),
    path('pesel/', views.validate_pesel)
]
