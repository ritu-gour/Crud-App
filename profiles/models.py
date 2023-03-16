from django.db import models

class Profile(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    password1=models.CharField(max_length=10)
    password2=models.CharField(max_length=10)