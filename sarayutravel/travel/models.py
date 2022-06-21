from tkinter import Pack
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Customer(models.Model):
    nameCustomer = models.CharField(max_length=100, null=True)
    emailCustomer = models.CharField(max_length=200)

    def __str__(self):
        return "{}".format(self.emailCustomer)

class Package(models.Model):
    namePackage = models.CharField(max_length=50)
    pricePackage = models.FloatField(max_length=10)
    cityPackage = models.CharField(max_length=50, null=True)
    countryPackage = models.CharField(max_length=50, default='Indonesia')
    imagePackage = models.ImageField(upload_to='packages/', default='default-packages.jpg')
    availablePackage = models.IntegerField(default=1)
    descriptionPackage = models.TextField(max_length=500, null=True)
    LIST_PACKAGE = (
        ('Honeymoon Package', 'Honeymoon Package'),
        ('Family Package', 'Family Package'),
        ('Holiday Package', 'Holiday Package'),
        ('Regular Package', 'Regular Package'),
    )
    categoryPackage = models.CharField(max_length=50, choices=LIST_PACKAGE, default='Regular Package')
    daysPackage = models.IntegerField(default=1)
    startPackage = models.DateField(auto_now_add=False, null=True)
    endPackage = models.DateField(auto_now_add=False, null=True)
    addonPackage = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return "{} - Rp.{}".format(self.namePackage, self.pricePackage)

    @property
    def imagePackages(self):
        try:
            url = self.imagePackage.url
        except:
            url = ''
        return url

class CustomPackage(models.Model):
    nameCustomPackage = models.CharField(max_length=200)
    emailCustomPackage = models.EmailField(max_length=200)
    phoneCustomPackage = models.CharField(max_length=25)
    guestCustomPackage = models.IntegerField(null=True)
    placeCustomPackage = models.CharField(max_length=200)
    LIST_SELECTEDCUSTOMPACKAGE = (
        ('Honeymoon Package', 'Honeymoon Package'),
        ('Family Package', 'Family Package'),
        ('Holiday Package', 'Holiday Package'),
        ('Regular Package', 'Regular Package'),
    )
    selectedCustomPackage = models.CharField(max_length=50, choices=LIST_SELECTEDCUSTOMPACKAGE, default="Regular Package")
    arrivalCustomPackage = models.DateField(auto_now_add=False, null=True, blank=True)
    departureCustomPackage = models.DateField(auto_now_add=False, null=True, blank=True)
    minpriceCustomPackage = models.FloatField(default=0, null=True)
    maxpriceCustomPackage = models.FloatField(default=0, null=True)
    dateCustomPackage = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}. {} - {} ({})".format(self.id, self.arrivalCustomPackage, self.departureCustomPackage, self.emailCustomPackage)

class Payment(models.Model):
	transactionId = models.CharField(max_length=100, null=True)
	pricePayment = models.FloatField(default=0, null=True)
	statusPayment = models.CharField(max_length=50, null=True)
	methodPayment = models.CharField(max_length=100, null=True)
	datePayment = models.DateTimeField(auto_now_add=True)
	completePayment = models.BooleanField(default=False)

	def __str__(self):
		return "{}. {} - {} Rp.{}".format(self.id, self.transactionId, self.statusPayment, self.pricePayment)

class Booking(models.Model):
    customerBooking = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    packageBooking = models.ForeignKey(Package, on_delete=models.SET_NULL, null=True, blank=True)
    paymentBooking = models.ForeignKey(Payment, on_delete=models.SET_NULL, null=True, blank=True)
    codeBooking = models.CharField(max_length=100, null=True)
    phoneBooking = models.CharField(max_length=25)
    emailBooking = models.EmailField(max_length=100)
    priceBooking = models.FloatField(default=0, null=True)
    dateBooking = models.DateTimeField(auto_now_add=True)
    completeBooking = models.BooleanField(default=False)

    def __str__(self):
        return "{}. {} - {} ({})".format(self.id, self.customerBooking, self.packageBooking, self.dateBooking)
        
class Testimonial(models.Model):
    nameTestimonial = models.CharField(max_length=100, null=True)
    commentTestimonial = models.TextField(max_length=500)
    dateTestimonial = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} ({})".format(self.nameTestimonial, self.dateTestimonial)

class Contact(models.Model):
    nameContact = models.CharField(max_length=100, null=True)
    emailContact = models.EmailField(max_length=200, null=True)
    phoneContact = models.CharField(max_length=20, null=True)
    subjectContact = models.CharField(max_length=100, null=True)
    messageContact = models.TextField(max_length=500, null=True)
    statusContact = models.BooleanField(default='False')
    dateContact = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}. {} ({})".format(self.id, self.nameContact, self.emailContact)