import requests
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


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    icon = models.ImageField(upload_to='category_image/', blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE,
                               related_name='subcategories',
                               blank=True,
                               null=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.name}'

    def is_root_category(self):
        return self.parent is None


class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    is_on_sale = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='product_images')

    def __str__(self):
        return f'{self.name}'









