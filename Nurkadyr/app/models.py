from django.db import models

# Create your models here.
class User1(models.Model):
     name = models.CharField(max_length = 120,unique=True)
     surname = models.CharField(max_length = 120,unique=True)
     email = models.EmailField()
     def __str__(self):
         return self.name
