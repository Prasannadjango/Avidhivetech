from django.contrib import admin
from .models import Products
from.models import Order
from.models import Signup

admin.site.register(Products)

admin.site.register(Signup)

admin.site.register(Order)
