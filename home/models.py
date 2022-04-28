from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    issue=models.TextField()
    date=models.DateField()


class Contribute(models.Model):
    name=models.CharField(max_length=120)
    email=models.CharField(max_length=120)
    contact=models.CharField(max_length=120)
    contribution=models.TextField()
    center=models.CharField(max_length=120)
    date=models.DateField()

class Joinus(models.Model):
    name=models.CharField(max_length=120)
    email=models.CharField(max_length=120)
    contact=models.CharField(max_length=120)
    DOB=models.DateField()
    reason=models.TextField()
    gender=models.CharField(max_length=20,default='not specified')
    city=models.CharField(max_length=120)
    state=models.CharField(max_length=120)
    occupation=models.CharField(max_length=120)
    
    Request_date=models.DateField()