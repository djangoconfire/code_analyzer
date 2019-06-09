from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    def _create_user(self, username, email,
                     password, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(
            username=username, email=email, **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password,
                                 **extra_fields)


class UserAuth(models.Model):
    user = models.OneToOneField(
        User, related_name="user_auth", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=100, null=True, blank=True)

    objects = UserManager()

    def __str__(self):
        return "{}".format(self.user.username)
