from django.shortcuts import render
from .models import MyModel
from .serializers import MySerialiuzer
# Create your views here.
from rest_framework import viewsets

class MyViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MySerialiuzer
    