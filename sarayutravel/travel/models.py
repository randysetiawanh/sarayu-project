from django.db import models
from django.contrib.auth.models import User

class Package(models.Model):
    namePackage = models.CharField(max_length=50)
    pricePackage = models.FloatField(max_length=10)
    imagePackage = models.ImageField(default='default-package.png')
    availablePackage = models.IntegerField(default=1)
    descriptionPackage = models.TextField(max_length=500, default="Ini Description")

    def __str__(self):
        return "{} - Rp.{}".format(self.namePackage, self.pricePackage)

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