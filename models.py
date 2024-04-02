from django.db import models

class User(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    birthdate=models.DateField()
    address=models.TextField()
