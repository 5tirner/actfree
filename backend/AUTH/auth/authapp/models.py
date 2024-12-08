from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class UserInfo(AbstractBaseUser):
    # Important
    firstname = models.CharField(max_length=20, null=False)
    lastname  = models.CharField(max_length=20, null=False)
    username  = models.CharField(max_length=20, null=False)
    email     = models.EmailField(unique=True, null=False)
    brithdate = models.DateField(null=False)
    password  = models.CharField(max_length=1000, null=False)
    # Not
    picture   = models.ImageField(null=True)
    country   = models.CharField(max_length=100, null=True)
    city      = models.CharField(max_length=100, null=True)
    # REQUIRED FIELDS
    USERNAME_FIELD = "email"
