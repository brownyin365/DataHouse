from django.contrib import admin
from .models import CustomerEmail, CustomerNumber

# Register your models here.

admin.site.register(CustomerEmail)
admin.site.register(CustomerNumber)
