from django.db import models
import enum# Create your models here.
class Note(models.Model):
    # La izquieda base de datos - derecha usuario
    status_choices = [
        ("ns", "no_status"),
        ("td", "to_do"),
        ("ip","in_progress"),
        ("cp","complete"),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(choices=status_choices,max_length=2)