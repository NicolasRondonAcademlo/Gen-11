from rest_framework import serializers
from .models import MyModel
from core.serializers import MinimunUserSerializer


class MySerialiuzer(serializers.ModelSerializer):
    owner = MinimunUserSerializer()
    class Meta:
        fields = "__all__"
        model = MyModel