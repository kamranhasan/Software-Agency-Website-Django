from django.contrib import admin
from .models import Service,Product, Package,Contact,ServiceBooking, ProductBooking,PackageBooking
# Register your models here.
admin.site.register(Service)
admin.site.register(Product)
admin.site.register(Package)
admin.site.register(Contact)
admin.site.register(ServiceBooking)
admin.site.register(ProductBooking)
admin.site.register(PackageBooking)