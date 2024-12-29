from app1 import views 
from django.urls import path 

urlpatterns = [
    path('main/', views.main, name="main"),
    path('', views.filterInDjango, name="filterInDjango"),
]
