from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .modelsHelper import userCreation

class UserInfo(AbstractBaseUser, PermissionsMixin):
    # Important
    firstname = models.CharField(max_length=50, null=False)
    lastname  = models.CharField(max_length=50, null=False)
    username  = models.CharField(max_length=50, null=False)
    email     = models.EmailField(unique=True, null=False)
    password  = models.CharField(max_length=1000, null=False)
    isAuth    = models.BooleanField(default=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['password']
    objects = userCreation()

    def __str__(self):
        return self.email

class UserActivation(models.Model):
    email = models.EmailField(null=False)
    verfCode = models.CharField(max_length=8)
