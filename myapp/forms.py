from django import forms
from .models import Contact,ServiceBooking,ProductBooking,PackageBooking
from django.db import models


class Messages(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email','subject', 'message' )

class ServiceBookings(forms.ModelForm):
    class Meta:
        model = ServiceBooking
        fields = ('Service_Name', 'Your_Name','email', 'Mobile_Number', 'message')

class ProductBookings(forms.ModelForm):
    class Meta:
        model = ProductBooking
        fields = ('Product_Name', 'Your_Name','email', 'Mobile_Number', 'message')

class PackageBookings(forms.ModelForm):
    class Meta:
        model = PackageBooking
        fields = ('Package_Name', 'Your_Name','email', 'Mobile_Number', 'message')

