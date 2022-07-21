from .models import Note
from rest_framework import serializers
from django.contrib.auth.models import User
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Note


class NoteSerializerCustom(serializers.ModelSerializer):
    title_custom = serializers.SerializerMethodField()
    class Meta:
        fields = "__all__"
        model = Note

    def get_title_custom(self, obj):
        return obj.title.upper()

class NoteSerializerCreate(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Note


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = User