from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import datetime
from .models import Food

def hello_world(reqest):
    hello = "Hola Gen 11"
    html = f"<html><h1>{hello}</h1></html>"
    return HttpResponse(html)

def all_fruits(request):
    food = Food.objects.all()
    print(food)
    names = food.values()
    #names = food.values_list("name", flat=True)
    print(names)
    result_list_name = []
    for name in names:
        text = f"<li>{name['name'] }-{name['quantity']}-{name['description']}</li>"
        result_list_name.append(text)

    result_list_string = ""
    for i in result_list_name:
        result_list_string += i
    result_list = f"<ul>{result_list_string}</ul>"
    return HttpResponse(result_list)