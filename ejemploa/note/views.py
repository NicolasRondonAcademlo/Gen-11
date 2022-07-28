from django.shortcuts import render
from rest_framework import viewsets
from .models import Note
from .serializers import NoteSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import  IsOwnerOrReadOnly
# Create your views here.

class NoteVieSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = [AllowAny]
            return [permission() for permission in self.permission_classes]
        else:
            self.permission_classes = [IsAuthenticated,  IsOwnerOrReadOnly]
            return [permission() for permission in self.permission_classes]
