from django.db import models

# Create your models here.

class Wilaya(models.Model):
    nom = models.CharField(max_length=100)

