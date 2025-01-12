from app1 import views 
from django.urls import path 

urlpatterns = [
    path('', views.main, name="main"),
    path('about/', views.about, name="about"),
    path('contact/', views.contactUs, name="contact"),
    path('register/', views.register, name="register"),
]
