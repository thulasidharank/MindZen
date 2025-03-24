from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('staff-augmentation/', views.staff_augmentation, name='staff_augmentation'),
    path('development-services/', views.development_services, name='development_services'),
    path('it-infrastructure-services/', views.it_infrastructure_services, name='it_infrastructure_services'),
    path('design-services/', views.design_services, name='design_services'),
]

