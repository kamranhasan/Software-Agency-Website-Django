from django.db import models

# Create your models here.
class Service(models.Model):
    name=models.CharField(max_length=300)
    picture=models.ImageField()
    description=models.CharField(max_length=1000)
    included=models.CharField(max_length=1500)
    Pricing=models.CharField(max_length=100,default='')
    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=300)
    picture=models.ImageField()
    description=models.CharField(max_length=1000)
    included=models.CharField(max_length=1500)
    Pricing=models.CharField(max_length=100,default='')
    features=models.CharField(max_length=1000,default='')
    Demo_link=models.CharField(max_length=500, default='')
    def __str__(self):
        return self.name


class Package(models.Model):
    name=models.CharField(max_length=300)
    picture=models.ImageField()
    Pricing=models.CharField(max_length=100,default='')
    def __str__(self):
        return self.name


class Contact(models.Model):
    name=models.CharField(max_length=150)
    email=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)
    message=models.CharField(max_length=400)
    def __str__(self):
        return self.name

class ServiceBooking(models.Model):
    Service_Name=models.CharField(max_length=150)
    Your_Name=models.CharField(max_length=150)
    email=models.CharField(max_length=100)
    Mobile_Number=models.CharField(max_length=50)
    message=models.CharField(max_length=400,default='')
    def __str__(self):
        return self.Service_Name


class ProductBooking(models.Model):
    Product_Name=models.CharField(max_length=150)
    Your_Name=models.CharField(max_length=150)
    email=models.CharField(max_length=100)
    Mobile_Number=models.CharField(max_length=50)
    message=models.CharField(max_length=400,default='')
    def __str__(self):
        return self.Product_Name


class PackageBooking(models.Model):
    Package_Name=models.CharField(max_length=150)
    Your_Name=models.CharField(max_length=150)
    email=models.CharField(max_length=100)
    Mobile_Number=models.CharField(max_length=50)
    message=models.CharField(max_length=400,default='')
    def __str__(self):
        return self.Package_Name