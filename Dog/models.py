from django.contrib.auth import get_user_model
from django.db import models
from django.conf import settings

User = get_user_model()

class Breed(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Trait(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class HealthStatus(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Dog(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="dogs/")

    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)

    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    location = models.CharField(max_length=100)

    description = models.TextField()

    traits = models.ManyToManyField(Trait, related_name='dogs')
    health_status = models.ManyToManyField(HealthStatus, related_name='dogs')

    is_adopted = models.BooleanField(default=False)

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="dogs",
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class Adoption(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    residence = models.CharField(max_length=255)
    number_people = models.CharField(max_length=255)
    children = models.CharField(max_length=255)
    dog_stay_day = models.CharField(max_length=255)
    dog_sleep_night = models.CharField(max_length=255)
    dog_exercise = models.CharField(max_length=255)
    have_owned_dog = models.CharField(max_length=255)
    if_yes = models.CharField(max_length=255)
    have_you_ever = models.CharField(max_length=255)

    submitted_at = models.DateTimeField(auto_now_add=True)