from .models import Book, BookItem
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model =Book


class BookReadSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("name", "author")
        model =Book


class MemberSerializer:
    class Meta:
        fields = "email, first_name"


class BookItemSerializer(serializers.ModelSerializer):
    book = BookReadSerializer()
    member = MemberSerializer()
    class Meta:
        fields = "__all__"
        model =BookItem


class BookItemCreateSerializer(serializers.ModelSerializer):


    class Meta:
        fields = "__all__"
        model =BookItem

