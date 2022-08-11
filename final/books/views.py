from django.shortcuts import render
from rest_framework import  viewsets
from .models import Book, BookItem, User
from .permissions import IsLibraryUser, IsRentForAnother
from .serializers import BookSerializer, BookItemSerializer, BookItemCreateSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookItemViewSet(viewsets.ModelViewSet):
    queryset = BookItem.objects.all()
    serializer_class = BookItemSerializer
    permission_classes = [IsLibraryUser]

    def get_serializer_class(self):
        if self.action == "create" or self.action == "update":
            return BookItemCreateSerializer
        else:
            return  BookItemSerializer

    def get_permissions(self):
        if self.action ==  "update":
            permissions = [ IsRentForAnother]
            return [permission() for permission in permissions]
        else:
            return [IsLibraryUser()]

    def update(self, request, *args, **kwargs):
        if self.action == "update":
            if self.request.user.is_staff:
                partial = kwargs.pop('partial', False)
                instance = self.get_object()
                serializer = self.get_serializer(instance, data=request.data, partial=partial)
                serializer.is_valid(raise_exception=True)
                self.perform_update(serializer)

                if getattr(instance, '_prefetched_objects_cache', None):
                    # If 'prefetch_related' has been applied to a queryset, we need to
                    # forcibly invalidate the prefetch cache on the instance.
                    instance._prefetched_objects_cache = {}

                return Response(serializer.data)
            else:
                partial = kwargs.pop('partial', False)
                instance = self.get_object()
                data = {
                    "is_rent": request.data["is_rent"],
                    "member": request.data["member"]
                }
                if data["is_rent"]:
                    data["is_rent"] = False
                    data["member"] = None
                serializer = self.get_serializer(instance, data=data, partial=True)
                serializer.is_valid(raise_exception=True)
                self.perform_update(serializer)

                if getattr(instance, '_prefetched_objects_cache', None):
                    # If 'prefetch_related' has been applied to a queryset, we need to
                    # forcibly invalidate the prefetch cache on the instance.
                    instance._prefetched_objects_cache = {}

                return Response(serializer.data)

