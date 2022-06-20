from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.db.models import F
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.mail import EmailMultiAlternatives
from django.contrib import messages
from django.template.loader import render_to_string
import requests
import uuid
import midtransclient

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
    getAllPackage = Package.objects.all().annotate(countNights=F('daysPackage')-1)
    getNewPackage = Package.objects.all().annotate(countNights=F('daysPackage')-1).order_by('-id')[:3]

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

def BookingView(request, idDetailOrder):
    getPackageDetail = Package.objects.get(id=idDetailOrder)
    getUUID = uuid.uuid4().hex[:10].upper()

    if request.method == 'POST':
        if request.POST.get('phone'):
            getCustomer, created = Customer.objects.get_or_create(emailCustomer = request.POST.get('email'))
            getCustomer.nameCustomer = request.POST.get('name')
            getCustomer.save()

            getPost = Booking()
            getPost.customerBooking = getCustomer
            getPost.packageBooking = getPackageDetail
            getPost.phoneBooking = request.POST.get('phone')
            getPost.emailBooking = request.POST.get('email')
            getPost.codeBooking = getUUID
            getPost.priceBooking = getPackageDetail.pricePackage
            getPost.save()
            messages.success(request, 'Your booking is created! Please make payment!')
            return redirect('/make_payment/'+getUUID)

    context = {
        'Type' : 'Booking Detail',
        'PackageDetail' : getPackageDetail,
        'CodeBooking' : getUUID,
    }
    return render(request, 'travel/booking_detail.html', context)

def MakePaymentView(request, idMakePayment):
    getBooking = Booking.objects.get(codeBooking=idMakePayment)
    getSnap  = midtransclient.Snap(
        is_production=False,
        server_key='SB-Mid-server-k667wrTSufdyQh36KeGUfZDT',
        client_key='SB-Mid-client-iT9YZECZAjAjTewG'
    )
    getParam = {
        "transaction_details": {
            "order_id": str(idMakePayment),
            "gross_amount": float(getBooking.priceBooking)
        }, "credit_card":{
            "secure" : True
        }
    }
    getTransaction = getSnap.create_transaction(getParam)
    getTransactionToken = getTransaction['token']
    print(getTransactionToken)
    print(getTransaction)

    context = {
        'Type' : 'Payment Page',
        'TransactionToken' : getTransactionToken,
        'Booking' : getBooking,
        'CodeBooking' : idMakePayment,
    }
    return render(request, 'travel/make_payment.html', context)

def ProcessBookingView(request, idBooking):
    getBookingData, created = Booking.objects.get_or_create(codeBooking=idBooking)
    
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Basic U0ItTWlkLXNlcnZlci1rNjY3d3JUU3VmZHlRaDM2S2VHVWZaRFQ='
    }
    getPayment = requests.get('https://api.sandbox.midtrans.com/v2/'+ idBooking +'/status', headers=headers)
    getDataPayment = getPayment.json()

    getPaymentData = Payment()
    getPaymentData.transactionId = getDataPayment['transaction_id']
    getPaymentData.pricePayment = getDataPayment['gross_amount']
    getPaymentData.statusPayment = getDataPayment['transaction_status']
    getPaymentData.methodPayment = getDataPayment['payment_type']
    if getPaymentData.statusPayment == 'settlement' or getPaymentData.statusPayment == 'capture':
        getPaymentData.completePayment = True
    else:
        getPaymentData.completePayment = False
    getPaymentData.save()

    if Payment.objects.filter(transactionId=getPaymentData.transactionId).exists():
        getBookingData.paymentBooking = getPaymentData
        getPackage, created = Package.objects.get_or_create(id=getBookingData.packageBooking.id)
        getPackage.availablePackage = getPackage.availablePackage - 1
        getPackage.save()
        getBookingData.save()

    getEmailData = { 'Booking' : getBookingData, }

    getHTML = render_to_string("travel/booking/email-confirmation.html", getEmailData)
    getMessage = EmailMultiAlternatives(
        subject = 'Booking Confirmation: ' + str(getBookingData.codeBooking),
        body="Booking Mail",
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[getBookingData.emailBooking],
        bcc=['randysetiawanh@gmail.com'],
    )
    getMessage.attach_alternative(getHTML, "text/html")
    getMessage.send(fail_silently=False)
    messages.success(request, 'Thank you for arranging a wonderful trip for us! Our team will contact you shortly!')

    return redirect('travel:package')

def PackageDetailView(request, idPackage):
    getPackageDetail = Package.objects.annotate(countNights=F('daysPackage')-1).get(id=idPackage)

    context = {
        'Type' : 'Package Detail',
        'DetailPackage' : getPackageDetail,
    }
    return render(request, 'travel/detail_package.html', context)

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