from django.db import models
from rest_framework.permissions import AllowAny
# Create your models here.
class Carro(models.Model):
    modelo= models.CharField(max_length=100)
    ano = models.IntegerField()
    dono = models.CharField(max_length=100)