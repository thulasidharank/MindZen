from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('staff-augmentation/', views.staff_augmentation, name='staff_augmentation'),
    path('development-services/', views.development_services, name='development_services'),
]

