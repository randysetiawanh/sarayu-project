from django.db import models
from django.contrib.auth.models import User

class Package(models.Model):
    namePackage = models.CharField(max_length=50)
    pricePackage = models.FloatField(max_length=10)
    cityPackage = models.CharField(max_length=50)
    countryPackage = models.CharField(max_length=50, default='Indonesia')
    imagePackage = models.ImageField(upload_to='packages/', default='default-packages.jpg')
    availablePackage = models.IntegerField(default=1)
    descriptionPackage = models.TextField(max_length=500)

    def __str__(self):
        return "{} - Rp.{}".format(self.namePackage, self.pricePackage)

    @property
    def imagePackages(self):
        try:
            url = self.imagePackage.url
        except:
            url = ''
        return url

class Customer(models.Model):
    userCustomer = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    nameCustomer = models.CharField(max_length=100, null=True)
    emailCustomer = models.CharField(max_length=200)

    def __str__(self):
        return "{}".format(self.userCustomer)

class Testimonial(models.Model):
    customerTestimonial = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL)
    nameTestimonial = models.CharField(max_length=100, null=True)
    commentTestimonial = models.TextField(max_length=500)
    dateTestimonial = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} ({})".format(self.customerTestimonial, self.dateTestimonial)