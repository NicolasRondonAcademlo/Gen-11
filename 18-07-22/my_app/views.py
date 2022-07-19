from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
import datetime
from .models import Food
from django.views.decorators.csrf import csrf_exempt
import json

def hello_world(reqest):
    hello = "Hola Gen 11"
    html = f"<html><h1>{hello}</h1></html>"
    return HttpResponse(html)

@csrf_exempt
def all_fruits(request):
    if request.method == "GET":
        food = Food.objects.all()
        names = food.values()
        #names = food.values_list("name", flat=True)
        result_list_name = []
        for name in names:
            text = f"<li>{name['name'] }-{name['quantity']}-{name['description']}</li>"
            result_list_name.append(text)

        result_list_string = ""
        for i in result_list_name:
            result_list_string += i
        result_list = f"<ul>{result_list_string}</ul>"
        return HttpResponse(result_list)
    if request.method == "POST":
        data = json.loads(request.body)
        nueva = Food(
            name=data.get("name"),
            description=data["description"],
            quantity=data["quantity"]
        )
        nueva.save()
        last_fruit = Food.objects.all().last()
        return JsonResponse({
            "name": last_fruit.name,
            "uuid": last_fruit.uuid
        })

# Vamos a crear un modelo de mascotas y vamos a renderizar en el navegador
# nombre, edad, animal

# Vamos a crear un modelo de comida preparada  y vamos a renderizar
# Los ingredientes y tiempo de coccion