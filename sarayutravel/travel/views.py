from django.shortcuts import render

from .models import *

def IndexView(request):
    return render(request, 'travel/index.html')

def PackageView(request):
    getAllPackage = Package.objects.all()

    context = {
        'Package' : getAllPackage,
    }
    return render(request, 'travel/package.html', context)
    
def PackageDetailView(request, idPackage):

    return render(request, 'travel/package.html')

def AboutView(request):
    return render(request, 'travel/about.html')

def ContactusView(request):
    return render(request, 'travel/contactus.html')

def SigninView(request):
    return render(request, 'travel/signin.html')

def SignupView(request):
    return render(request, 'travel/signup.html')