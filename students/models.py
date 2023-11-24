from django.db import models

# Create your models here.
class student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=200)
    mobile = models.CharField(max_length=20)
    password = models.CharField(max_length=255)