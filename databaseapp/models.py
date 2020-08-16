from django.db import models
from django.contrib.auth.models import User
import birthday
import datetime


class UserInfo(models.Model):
    dob = models.DateField()
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
