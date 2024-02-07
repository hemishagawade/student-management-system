from django.db import models

# Create your models here.
class Student(models.Model):
    # id - auto genenrated
    name = models.CharField(max_length=30)
    branch = models.CharField(max_length=10)
    year = models.CharField(max_length=10)
    dob = models.DateField()
    phno = models.CharField(max_length=10)
    email = models.CharField(max_length=20)
