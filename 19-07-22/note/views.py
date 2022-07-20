from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from .models import Note
from .serializers import NoteSerializer, NoteSerializerCreate
from rest_framework.response import Response
from rest_framework import viewsets

class NoteListAPiView(generics.ListAPIView):
    queryset = Note.objects.all()
    serializer_class =  NoteSerializer

    # Para personalizar el metodo
    #def  list(self, request, *args, **kwargs):
    #    return Response({"message": "nada"})

class NoteCreateApiView(generics.CreateAPIView):
    queryset = Note.objects.all()
    serializer_class =  NoteSerializerCreate

class NoteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class =  NoteSerializer

class NoteRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class =  NoteSerializer

class NoteRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class =  NoteSerializer


# Vamos a crear el modelo de una persona y a hacer los endpoints necesarios
# para tener un CRUD de Personas

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer