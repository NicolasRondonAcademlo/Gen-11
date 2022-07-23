from django.db import models

from core.models import CustomUser
# Create your models here.
class MyModel(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField()
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)