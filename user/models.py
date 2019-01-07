from django.db import models
from django.contrib.auth.models import User
from chatsite.models import user
from django import forms
class new_feed(models.Model):
    #Email=models.ForeignKey(user,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    date=models.DateTimeField()
    data=models.CharField(max_length=1000)
