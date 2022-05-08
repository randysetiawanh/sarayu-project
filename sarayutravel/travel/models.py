from django.db import models
from django.contrib.auth.models import User

class Package(models.Model):
    namePackage = models.CharField(max_length=50)
    pricePackage = models.FloatField(max_length=10)
    imagePackage = models.ImageField(default='default-package.png')

    def __str__(self):
        return "{} - Rp.{}".format(self.namePackage, self.pricePackage)

class Customer(models.Model):
    userCustomer = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    nameCustomer = models.CharField(max_length=200, null=True)
    emailCustomer = models.CharField(max_length=200)

    def __str__(self):
        return "{}".format(self.userCustomer)