from django.contrib import admin

from .models import  Property, Tenant

# Register your models here.

admin.site.register(Property)
admin.site.register(Tenant)

