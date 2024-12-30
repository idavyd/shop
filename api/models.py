from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime as dt


class User(AbstractUser):
    pass


class Profile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(default=f'{dt.date.today()}', null=True, blank=False)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=3, null=True, blank=False)
    phone_number = models.CharField(max_length=13, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} - {self.user.username}'







