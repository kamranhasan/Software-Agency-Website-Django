from django.contrib import admin
from .models import Service,Product, Package
# Register your models here.
admin.site.register(Service)
admin.site.register(Product)
admin.site.register(Package)