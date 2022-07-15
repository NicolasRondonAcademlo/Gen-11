
from django.db import models
from django_softdelete.models import SoftDeleteModel
# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=152)

class Artist(models.Model):
    name = models.CharField(max_length=152)
    albums = models.ManyToManyField(Album)

# Many to one - Uno a muchos

class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

class Article(models.Model):
    headline = models.CharField(max_length=100)
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)


class Vehicle(SoftDeleteModel):
    name = models.CharField(max_length=150)
    color = models.CharField(max_length=150)


# Un sistema de modelos y relaciones donde pueda crear
# Quizzes (Por el momento no es necesario que tengan preguntas)
# Crear Personas
# ASignar Una persona con un quiz y un puntaje