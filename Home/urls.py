from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('staff-augmentation/', views.staff_augmentation, name='staff_augmentation'),
    path('development-services/', views.development_services, name='development_services'),
    path('it-infrastructure-services/', views.it_infrastructure_services, name='it_infrastructure_services'),
    path('design-services/', views.design_services, name='design_services'),
    path('managed-cloud-services/', views.managed_cloud_services, name='managed_cloud_services'),
    path('digital-marketing-services/', views.digital_marketing_services, name='digital_marketing_services'),
    path('genai-services/', views.genai_services, name='genai_services'),
    path('saas-services/', views.saas_services, name='saas_services'),
    path('application-development-services/', views.application_development_services, name='application_development_services'),
    path('legacy-modernization-services/', views.legacy_modernization_services, name='legacy_modernization_services'),
    path('erp-services/', views.erp_services, name='erp_services'),
    path('business-growth-services/', views.business_growth_services, name='business_growth_services'),
    path("contact/", views.contact_form, name="contact_form"),
]

