import uuid
from django.db import models

# Create your models here.

class Food(models.Model):
    name = models.CharField(max_length=150)
    quantity = models.IntegerField()
    uuid = models.UUIDField(default=uuid.uuid4)
    description = models.TextField()
