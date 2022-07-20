from .models import Note
from rest_framework import serializers

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Note

class NoteSerializerCreate(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Note
