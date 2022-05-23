from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    userCustomer = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
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

class Testimonial(models.Model):
    nameTestimonial = models.CharField(max_length=100, null=True)
    commentTestimonial = models.TextField(max_length=500)
    dateTestimonial = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} ({})".format(self.nameTestimonial, self.dateTestimonial)