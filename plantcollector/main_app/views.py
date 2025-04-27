from django.shortcuts import render
from django.http import HttpResponse

from .models import plants


# Create your views here.


def home(request):
    # Send a simple HTML response
    return HttpResponse("<h1>Hello ᓚᘏᗢ</h1>")


def plant_index(request):
    return render(request, "plant-index.html", {"plants": plants})


def about(request):
    return render(request, "about.html")
