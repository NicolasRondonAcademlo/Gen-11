from django.db import models
from django.contrib.auth.models import  User
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
    owner = models.ForeignKey(User, on_delete=models.CASCADE)