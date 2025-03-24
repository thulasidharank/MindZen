from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def staff_augmentation(request):
    return render(request, 'staff_augmentation.html')


def development_services(request):
    return render(request, 'development_services.html')

def it_infrastructure_services(request):
    return render(request, 'it_infrastructure_services.html')

def design_services(request):
    return render(request, 'design_services.html')

def managed_cloud_services(request):
    return render(request, 'managed_cloud_services.html')

def digital_marketing_services(request):
    return render(request, 'digital_marketing_services.html')