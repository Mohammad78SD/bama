from django.shortcuts import render
from .models import car
# Create your views here.


def list(request):
    cars = car.objects.all()
    cars_list = []
    for car in cars:
        dict = {
            "brand" : car.brand,
            "name" : car.name,
            "km" : car.km,
            "color" : car.color,
            "description" : car.description,
            "image" : car.image,
        }
        cars_list.append(dict)
        