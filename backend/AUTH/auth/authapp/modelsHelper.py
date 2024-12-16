from django.contrib.auth.models import BaseUserManager

class userCreation(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        userToAdd = self.model(email=email, **extra_fields)
        userToAdd.set_password(password)
        userToAdd.save(using=self._db)
        return userToAdd

    def create_superuser(self, email, password=None, **extra_fields):
        raise "Create Super User Is Totally Forbbeiden"
