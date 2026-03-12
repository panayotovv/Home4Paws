from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import UserManager

class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class User(AbstractUser):
    username = None

    image = models.ImageField(upload_to="avatars/", null=True, blank=True)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    location = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    roles = models.ManyToManyField(Role, blank=True)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name"]

    objects = UserManager()

