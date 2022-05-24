from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMultiAlternatives
from django.contrib import messages
from django.template.loader import render_to_string
import uuid

from .models import *
from .forms import CustomPackageForm

def IndexView(request):
    getNewPackage = Package.objects.all().order_by('-id')[:3]

    context = {
        'Type' : 'Home Sarayu',
        'NewPackage' : getNewPackage,
    }
    return render(request, 'travel/index.html', context)

def PackageView(request):
    getAllPackage = Package.objects.all()
    getNewPackage = Package.objects.all().order_by('-id')[:3]

    if request.method == 'POST':
        getForm = CustomPackageForm(request.POST)
        if getForm.is_valid():
            getForm.save()
            getSubject = 'Custom Booking from ' + getForm.cleaned_data['nameCustomPackage'] + ' - ' + getForm.cleaned_data['emailCustomPackage']
            body = {
            'nameCustomPackage': getForm.cleaned_data['nameCustomPackage'],
            'emailCustomPackage': getForm.cleaned_data['emailCustomPackage'],
            'phoneCustomPackage': str(getForm.cleaned_data['phoneCustomPackage']),
            'guestCustomPackage': str(getForm.cleaned_data['guestCustomPackage']),
            'placeCustomPackage': getForm.cleaned_data['placeCustomPackage'],
            'selectedCustomPackage': getForm.cleaned_data['selectedCustomPackage'],
            'arrivalCustomPackage': str(getForm.cleaned_data['arrivalCustomPackage']),
            'departureCustomPackage': str(getForm.cleaned_data['departureCustomPackage']),
            'minpriceCustomPackage': str(getForm.cleaned_data['minpriceCustomPackage']),
            'maxpriceCustomPackage': str(getForm.cleaned_data['maxpriceCustomPackage']),
            }
            getMessage = "\n".join(body.values())

            try:
                email = EmailMessage(getSubject, getMessage, settings.DEFAULT_FROM_EMAIL, [getForm.cleaned_data['emailCustomPackage']], ['randysetiawanh@gmail.com'])
                email.send(fail_silently=True)
                messages.success(request, 'Thank you for arranging a wonderful trip for us! Our team will contact you shortly!')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('travel:package')
    else:
        getForm = CustomPackageForm()

    context = {
        'Type' : 'Package',
        'Package' : getAllPackage,
        'NewPackage' : getNewPackage,
        'Form' : getForm,
    }
    return render(request, 'travel/package.html', context)
    
def PackageDetailView(request, idPackage):
    context = {
        'Type' : 'Package Detail',
    }
    return render(request, 'travel/package.html', context)

def BookingView(request, idDetailOrder):
    getPackageDetail = Package.objects.get(id=idDetailOrder)
    if request.method == 'POST':
        if request.POST.get('phone'):
            getEmail = request.POST.get('email')
            getName = request.POST.get('name')
            getCustomer, created = Customer.objects.get_or_create(emailCustomer = getEmail)
            getCustomer.nameCustomer = getName
            getCustomer.save()

            getUUID = uuid.uuid4()
            getPost = Booking()
            getPost.customerBooking = getCustomer
            getPost.packageBooking = getPackageDetail
            getPost.phoneBooking = request.POST.get('phone')
            getPost.transactionBooking = getUUID
            getPost.priceBooking = getPackageDetail.pricePackage
            getPost.save()

            getEmailData = {
                'Customer': getCustomer, 'PackageDetail': getPackageDetail, 'DateBooking': getPost.dateBooking,
                'Phone': request.POST.get('phone'), 'BookingCode': getPost.transactionBooking,
            }
            getHTML = render_to_string("travel/booking/email-confirmation.html", getEmailData)
            getMessage = EmailMultiAlternatives(
                subject = 'Booking Confirmation: ' + str(getPost.transactionBooking),
                body="Booking Mail",
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[getEmail],
                bcc=['randysetiawanh@gmail.com'],
            )
            getMessage.attach_alternative(getHTML, "text/html")
            getMessage.send(fail_silently=False)
            messages.success(request, 'Thank you for arranging a wonderful trip for us! Our team will contact you shortly!')
        return HttpResponseRedirect("/package/")

    context = {
        'Type' : 'Booking Detail',
        'PackageDetail' : getPackageDetail,
    }
    return render(request, 'travel/booking_detail.html', context)

def ProcessBookingView(request):
    pass

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