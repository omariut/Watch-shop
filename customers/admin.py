from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from customers.models import Customer
from orders.models import Address
from django.contrib.auth import get_user_model


# Register your models here.

admin.site.register(Customer)
admin.site.register(Address)