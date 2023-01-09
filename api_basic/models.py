from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# coffee machine parts

class Devices(models.Model):
    name = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Sells(models.Model):
    device = models.ForeignKey(Devices, on_delete=models.CASCADE)
    date = models.DateField()
    sell = models.IntegerField()

    def __str__(self):
        return self.device.name
