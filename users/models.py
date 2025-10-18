from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from users.managers import CustomUserManager


class CustomUser(AbstractUser):
    username = models.CharField(unique=True, max_length=50, verbose_name='Name', blank=True, null=True)
    #email = models.EmailField(unique=True, max_length=50, verbose_name='Email')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


