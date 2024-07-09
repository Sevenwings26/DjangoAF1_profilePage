from django.urls import path
from . import views

urlpatterns = [
    path('', views.landingPage, name="index"),
    path('vision-pg/', views.visionPage, name="vision"),
]