from django.db import models

# Create your models here.
class Company(models.Model):

    brand = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    products = models.CharField(max_length=150)
    
    def __str__(self):
        return self.brand