from django.shortcuts import render
from .models import Service, Product, Package
from .forms import Messages, ServiceBookings, ProductBookings, PackageBookings
# Create your views here.
def home(request):
    services = Service.objects.all()[:4]
    products = Product.objects.all()[:3]
    packages = Package.objects.all()[:3]
    return render(request, 'index.html',{'services': services,'products':products, 'packages':packages})

def packages(request):
    packages = Package.objects.all()
    return render(request, 'packages.html',{ 'packages':packages})

def services(request):
    services = Service.objects.all()
    return render(request, 'services.html',{'services': services,})

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html',{'products':products})


def about(request):
    products = Product.objects.all()
    return render(request, 'about.html',{'products':products})

def contact(request):
    message = Messages()
    respond = 'Send Message'
    return render(request, 'contact.html',{'message':message, 'respond': respond})


def contacted(request):
    if request.method=="POST":
        data=Messages(request.POST)
        if data.is_valid():
            data.save()
            # send_mail('New Contact Form Submission', request.POST['message'], 'nomadsadventureservice', ['nomadsadventureservice@gmail.com'], fail_silently=True)
            respond='Your Message has been sent successfully!'
            return render(request,'contact.html',{'respond':respond})
        else:
            data=Messages()
            respond='Your Message has been sent successfully!'
            return render(request,'contact.html',{'respond':respond})


def servicedetail(request,id):
    service=Service.objects.get(id=id)
    booking=ServiceBookings(initial={'Service_Name':service.name})
    respond='Hire Now!'
    return render(request, 'detailed.html',{'check':'yes','service': service, 'booking':booking, 'respond':respond })

def servicedetailed(request):
    # service=Service.objects.get(id=id)
    if request.method=="POST":
        data=ServiceBookings(request.POST)
        if data.is_valid():
            post=data.save()
            post.save()
            # send_mail('New Make My Own Trip Booking', request.POST['Your_Full_Name'], 'nomadsadventureservice', ['nomadsadventureservice@gmail.com'], fail_silently=True)
            respond='You have booked yourself this service successfully. You will be contacted by team ColonHash shortly!'
            return render(request,'detailed.html',{ 'check':'no','respond':respond })
        else:
            data=ServiceBookings()
            respond='You have booked yourself this service successfully. You will be contacted by team ColonHash shortly!'
            return render(request,'detailed.html',{'check':'no','respond':respond})
    else:
        respond='You have booked yourself this service successfully. You will be contacted by team ColonHash shortly!'
        return render(request,'detailed.html',{ 'check':'no', 'respond':respond })



def productdetail(request,id):
    product=Product.objects.get(id=id)
    booking=ProductBookings(initial={'Product_Name':product.name})
    respond='Buy Now!'
    return render(request, 'productdetail.html',{'check':'yes','product': product, 'booking':booking, 'respond':respond })


def productdetailed(request):
    # service=Service.objects.get(id=id)
    if request.method=="POST":
        data=ProductBookings(request.POST)
        if data.is_valid():
            post=data.save()
            post.save()
            # send_mail('New Make My Own Trip Booking', request.POST['Your_Full_Name'], 'nomadsadventureservice', ['nomadsadventureservice@gmail.com'], fail_silently=True)
            respond='You have booked yourself this Product successfully. You will be contacted by team ColonHash shortly!'
            return render(request,'productdetail.html',{ 'check':'no','respond':respond })
        else:
            data=ServiceBookings()
            respond='You have booked yourself this Product successfully. You will be contacted by team ColonHash shortly!'
            return render(request,'productdetail.html',{'check':'no','respond':respond})
    else:
        respond='You have booked yourself this Product successfully. You will be contacted by team ColonHash shortly!'
        return render(request,'Productdetail.html',{ 'check':'no', 'respond':respond })



def packagedetail(request,id):
    package=Package.objects.get(id=id)
    booking=PackageBookings(initial={'Package_Name':package.name})
    respond='Buy Now!'
    return render(request, 'packagedetail.html',{'check':'yes','package': package, 'booking':booking, 'respond':respond })


def packagedetailed(request):
    # service=Service.objects.get(id=id)
    if request.method=="POST":
        data=PackageBookings(request.POST)
        if data.is_valid():
            post=data.save()
            post.save()
            # send_mail('New Make My Own Trip Booking', request.POST['Your_Full_Name'], 'nomadsadventureservice', ['nomadsadventureservice@gmail.com'], fail_silently=True)
            respond='You have booked yourself this Package successfully. You will be contacted by team ColonHash shortly!'
            return render(request,'packagedetail.html',{ 'check':'no','respond':respond })
        else:
            data=ServiceBookings()
            respond='You have booked yourself this Package successfully. You will be contacted by team ColonHash shortly!'
            return render(request,'packagedetail.html',{'check':'no','respond':respond})
    else:
        respond='You have booked yourself this Package successfully. You will be contacted by team ColonHash shortly!'
        return render(request,'packagedetail.html',{ 'check':'no', 'respond':respond })
