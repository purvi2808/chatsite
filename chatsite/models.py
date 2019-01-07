from django.db import models
from django import forms
from django.contrib.auth.models import User


class user(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username','password']
