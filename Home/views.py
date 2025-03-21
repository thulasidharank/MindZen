from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def staff_augmentation(request):
    return render(request, 'staff_augmentation.html')