from django.db import models

# Create your models here.
from books.models import BookItem


class Rack(models.Model):
    hallway = models.IntegerField()
    category = models.CharField(max_length=150)

    def __str__(self):
        return  f"{self.category} ---- hall {self.hallway}"

class RackBookItem(models.Model):
    rack = models.ForeignKey(Rack, on_delete=models.CASCADE)
    book_item = models.ForeignKey(BookItem, on_delete=models.CASCADE)
    floor = models.IntegerField()

    def __str__(self):
        return f" hall {self.rack.hallway} --- {self.book_item.book.name}"