from django.shortcuts import render
from .serializers import UserSerializer, CreateUserSerializer
from .models import CustomUser
from rest_framework import viewsets
# Create your views here.

class CustomUserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    
    def get_serializer_class(self):
        if self.action == "create":
            return UserSerializer
        else:
            return UserSerializer
