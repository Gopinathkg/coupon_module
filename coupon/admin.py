from django.contrib import admin
from .models import UserRegistration, Referral

# Register your models here.

admin.site.register(UserRegistration)
admin.site.register(Referral)
