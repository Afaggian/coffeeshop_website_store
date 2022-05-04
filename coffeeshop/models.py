from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from coffeeshop.validators import validate_postcode
from .utils import *

class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, null=True)

    def __str__(self):
        return self.username


class UserDetails(models.Model):
    username = models.CharField(max_length=100)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, validators=[MinLengthValidator(10)], default=0)
    email = models.EmailField(max_length=100)
    postcode = models.CharField(max_length=100, validators=[validate_postcode], default=0)
    address = models.CharField(max_length=300)

    def __str__(self):
        return self.username

class Coffee(models.Model):
    name = models.CharField(max_length=10, choices=COFFEE_CHOICES)
    size = models.CharField(max_length=1, choices=SIZE_CHOICES)
    quantity = models.CharField(max_length=1, choices=QUANTITY_CHOICES)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name