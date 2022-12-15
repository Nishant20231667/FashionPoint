from django.urls import path
from . import views

urlpatterns = [
    
    path('brands/', views.brands, name="brands"),
    path('', views.home, name="home"),
    path('contactus/', views.contactus, name="contactus"),
    path('contactus/home', views.home, name="home"),
    path('contactus/brand', views.brand, name="brand"),
]
