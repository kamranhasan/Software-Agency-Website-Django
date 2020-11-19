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
    def __str__(self):
        return self.name


class Package(models.Model):
    name=models.CharField(max_length=300)
    picture=models.ImageField()
    Pricing=models.CharField(max_length=100,default='')
    def __str__(self):
        return self.name