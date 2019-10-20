from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Passwordresetcodes(models.Model):
    code = models.CharField(max_length=32)
    email = models.CharField(max_length=120)
    time = models.DateTimeField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)  # TODO: do not save password


class Expense(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{} --- {} ---> {}".format(self.date, self.text, self.amount)


class Income(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{} --- {} ---> {}".format(self.date, self.text, self.amount)


class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=45)

    def __str__(self):
        return '{} -- token'.format(self.user)
