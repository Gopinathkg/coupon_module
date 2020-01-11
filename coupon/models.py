import uuid

from django.db import models
from random import randint


# Create your models here.

class UserRegistration(models.Model):
    objects = None
    CHENNAI = "ch"
    VELLORE = "VE"
    BANGLORE = "BE"
    CITIES = (
        (CHENNAI, "Chennai"),
        (VELLORE, "Vellore"),
        (BANGLORE, "Banglore"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128)
    age = models.IntegerField()
    city = models.CharField(max_length=2, choices=CITIES, blank=True)
    coupon = models.CharField(max_length=7, default=randint(1234567, 7654321), unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Referral(models.Model):
    objects = None
    CHENNAI = "ch"
    VELLORE = "VE"
    BANGLORE = "BE"
    CITIES = (
        (CHENNAI, "Chennai"),
        (VELLORE, "Vellore"),
        (BANGLORE, "Banglore"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    reference_id = models.ForeignKey(UserRegistration, on_delete=models.CASCADE, )
    reference = models.BooleanField(default=True)
    name = models.CharField(max_length=128)
    age = models.IntegerField()
    city = models.CharField(max_length=2, choices=CITIES, blank=True)
    reference_coupon = models.CharField(max_length=7, unique=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
