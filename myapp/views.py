from django.shortcuts import render
from .models import Service, Product, Package
# Create your views here.
def home(request):
    services = Service.objects.all()[:4]
    products = Product.objects.all()[:3]
    packages = Package.objects.all()[:3]
    return render(request, 'index.html',{'services': services,'products':products, 'packages':packages})
