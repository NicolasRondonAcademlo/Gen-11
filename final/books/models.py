import uuid as uuid
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import  uuid
# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=80, null=False)
    author = models.CharField(max_length=80, null=False)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return  self.name


class BookItem(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=False)
    member = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    uuid = models.UUIDField(default=uuid.uuid4())
    is_rent = models.BooleanField(default=False)
    is_reserve = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return  self.book.name + f" --- id {self.id}"

@receiver(post_save, sender=BookItem)
def update_available(sender, instance, **kwargs):
    if not kwargs["created"]:
        if instance.is_rent:
            is_available = False
        else:
            is_available =True

        BookItem.objects.filter(pk=instance.id).update(is_available=is_available)
