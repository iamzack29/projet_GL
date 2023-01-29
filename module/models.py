from django.db import models

# Create your models here.
class matiere(models.Model):
	nom = models.CharField(max_length=50)