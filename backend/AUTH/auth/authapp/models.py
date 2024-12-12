from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class userCreation(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        pass

    def create_superuser(self, email, password=None, **extra_fields):
        raise "Create Super User Is Totally Forbbeiden"
class UserInfo(AbstractBaseUser):
    # Important
    firstname = models.CharField(max_length=20, null=False)
    lastname  = models.CharField(max_length=20, null=False)
    username  = models.CharField(max_length=20, null=False)
    email     = models.EmailField(unique=True, null=False)
    birthdate = models.DateField(null=False)
    password  = models.CharField(max_length=1000, null=False)
    # Not
    picture   = models.ImageField(null=True)
    country   = models.CharField(max_length=100, null=True)
    city      = models.CharField(max_length=100, null=True)
    # REQUIRED FIELDS
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['password']
    objects = userCreation()
