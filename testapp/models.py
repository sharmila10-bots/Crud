from django.db import models

# Create your models here.
class Book(models.Model):
    bno=models.IntegerField()
    bname=models.CharField(max_length=100)
    bauthor=models.CharField(max_length=25)
    byear=models.IntegerField()
    
