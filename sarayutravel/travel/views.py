from django.shortcuts import render

from .models import *

def IndexView(request):
    context = {
        'Type' : 'Home Sarayu',
    }
    return render(request, 'travel/index.html', context)

def PackageView(request):
    getAllPackage = Package.objects.all()

    context = {
        'Type' : 'Package',
        'Package' : getAllPackage,
    }
    return render(request, 'travel/package.html', context)
    
def PackageDetailView(request, idPackage):
    context = {
        'Type' : 'Package Detail',
    }
    return render(request, 'travel/package.html', context)

def AboutView(request):
    context = {
        'Type' : 'About',
    }
    return render(request, 'travel/about.html', context)

def ContactusView(request):
    context = {
        'Type' : 'Contact Us',
    }
    return render(request, 'travel/contactus.html', context)

def SigninView(request):
    context = {
        'Type' : 'Sign In',
    }
    return render(request, 'travel/signin.html', context)

def SignupView(request):
    context = {
        'Type' : 'Sign Up',
    }
    return render(request, 'travel/signup.html', context)