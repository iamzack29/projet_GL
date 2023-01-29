from django.db import models

from wilaya.models import Wilaya

# Create your models here.
class Commune(models.Model):
    Wilaya= models.ForeignKey(Wilaya,on_delete=models.CASCADE,related_name='wilaya')
    nom = models.CharField(max_length=100)