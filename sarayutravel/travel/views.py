from django.shortcuts import render

from .models import *

def IndexView(request):
    context = {
        'Type' : 'Home Sarayu',
    }
    return render(request, 'travel/index.html', context)

def PackageView(request):
    getAllPackage = Package.objects.all()
    getNewPackage = Package.objects.all().order_by('-id')[:3]
    context = {
        'Type' : 'Package',
        'Package' : getAllPackage,
        'NewPackage' : getNewPackage,
    }
    return render(request, 'travel/package.html', context)
    
def PackageDetailView(request, idPackage):
    context = {
        'Type' : 'Package Detail',
    }
    return render(request, 'travel/package.html', context)

def AboutView(request):
    getNewTestimonial = Testimonial.objects.all().order_by('-id')[:4]
    context = {
        'Type' : 'About',
        'NewTestimonial' : getNewTestimonial,
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