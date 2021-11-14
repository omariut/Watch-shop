from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class Customer (AbstractUser):
    name = models.CharField(max_length=20)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


    

