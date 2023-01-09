from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


# Create your models here.
# Django's signal system  create a new Token object every time a ' \
# 'new User object is saved to the database
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Machine(models.Model):
    name = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    serial_no = models.CharField(max_length=100)
    # owner works on primary key
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Sell(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    date = models.DateField()
    sell = models.IntegerField()

    def __str__(self):
        return self.machine.name


class SellRange(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
