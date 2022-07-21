from .models import Note
from rest_framework import serializers
from django.contrib.auth.models import User
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Note


class NoteSerializerCreate(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Note


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = User