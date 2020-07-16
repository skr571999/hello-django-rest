from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from .managers import UserManager

GENDERS = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
]


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    father_name = models.CharField(max_length=50, null=True, blank=True)
    mobile_no = models.BigIntegerField(unique=True, null=True, blank=True)
    country = models.ForeignKey(
        'Country',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    home_address = models.TextField(max_length=300, blank=True, null=True)
    aadhar_no = models.BigIntegerField(blank=True, null=True)
    pan_no = models.BigIntegerField(blank=True, null=True)
    gender = models.CharField(
        max_length=1, choices=GENDERS, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    # only for django admin panel
    is_staff = models.BooleanField(default=False)
    company = models.ForeignKey(
        'Company',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    objects = UserManager()

    REQUIRED_FIELDS = ['name']
    USERNAME_FIELD = 'email'


class Country(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=100)


class Company(models.Model):
    name = models.CharField(max_length=200)
    # type = models.CharField()
    mobile_no1 = models.BigIntegerField(unique=True)
    mobile_no2 = models.BigIntegerField(unique=True, blank=True, null=True)
    pan_no = models.BigIntegerField(blank=True, null=True)
    gst_no = models.BigIntegerField(blank=True, null=True)
    cin_no = models.BigIntegerField(blank=True, null=True)
    is_seller = models.BooleanField(default=False)
