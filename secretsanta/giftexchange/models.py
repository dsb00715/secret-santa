from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class GiftExchange(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()


class Participant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gift_exchange = models.ForeignKey(GiftExchange, on_delete=models.CASCADE)
