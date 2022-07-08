from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=250)
    age = models.IntegerField()
    is_live = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.name}  {self.age}"