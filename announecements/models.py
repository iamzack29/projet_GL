from django.db import models
from simpleuser.models import Account
from module.models import matiere
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class annonce(models.Model):
    owner = models.ForeignKey(Account , on_delete=models.CASCADE , related_name="organisation",limit_choices_to={'is_teacher': True})
    title = models.CharField(max_length=100,blank=True,null=True)
    module = models.ForeignKey(matiere,on_delete=models.CASCADE, related_name="module")
    duration         = models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(3)])
    date 		 = models.TimeField(blank=True , null=True)
    description = models.TextField(blank=True, null=True)