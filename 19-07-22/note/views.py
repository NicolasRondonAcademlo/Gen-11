from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from .models import Note
from .serializers import NoteSerializer, NoteSerializerCreate,UserSerializer, NoteSerializerCustom
from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
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


        # Un detalle es cuando acceso solo a un elemento
    @action(detail=False)
    def all_complete_notes(self, request):
        notes =self.get_queryset()
        notes_complete = notes.filter(status="cp")
        serializer = self.get_serializer_class()
        data = serializer(notes_complete, many=True)
        return Response({"data": data.data})

    @action(detail=False)
    def my_notes_convert(self, request):
        notes =self.get_queryset()
        for note in notes:
            note.title = note.title.upper()
            note.description = note.description.upper()
        serializer = self.get_serializer_class()
        data = serializer(notes, many=True)
        return Response({"data": data.data})

    @action(detail=False)
    def my_notes_convert_custom(self, request):
        notes =self.get_queryset()
        serializer = NoteSerializerCustom
        data = serializer(notes, many=True)
        return Response({"data": data.data})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    @action(detail=True, methods=["get", "post"])
    def my_notes(self, request, pk=None):
        all_notes = Note.objects.filter(owner=pk)
        serializer = NoteSerializer(all_notes, many=True)
        if request.method== "POST":
            request.data["owner"]=pk
            self.serializer_class = NoteSerializer
            self.queryset = Note.objects.all()
            serializer = self.serializer_class
            serializer = serializer(data=request.data)
            if serializer.is_valid():
               serializer.save()
               return Response({"data":serializer.data})
            else:
                print("aaa")
                return Response({"error": serializer.errors})
    
        return Response({"data":serializer.data})



# Vamos a crear acciones para ver las notas por cada estado
# Vamos a crear una accion que me permita ver la ultima nota agregada por un usuario
# vamos a crear una accione que me regrese tres notas aleatorias
# vamos a crear una accion que regrese las notas pero donde el titulo y descripcion
# las vocales sean remplazadas por a=1 e=2 i=3 o=4 u=5
# Hola -> H4l1
# Vamos a crear una accion para ver la primer nota agregada por un usuario
# Vamos a crear una accion para devolver todos los usuarios activos
# vamos a crear una accion para devolver todos los usuarios inactivos
# vamos a crear una accion para devolver las notas de un usuario