from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Plant
from .forms import WateringForm


# Create your views here.


def home(request):
    # Send a simple HTML response
    return render(request, "home.html")


def plant_index(request):
    plants = Plant.objects.all()
    return render(request, "plants/index.html", {"plants": plants})


def about(request):
    return render(request, "about.html")


def plant_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    watering_form = WateringForm()
    return render(
        request, "plants/details.html", {"plant": plant, "watering_form": watering_form}
    )


def add_watering(request, plant_id):
    # create a ModelForm instance using the data in request.POST
    form = WateringForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the plant_id assigned
        new_feeding = form.save(commit=False)
        new_feeding.plant_id = plant_id
        new_feeding.save()
    return redirect("plant-detail", plant_id=plant_id)


class PlantCreate(CreateView):
    model = Plant
    fields = "__all__"


class PlantUpdate(UpdateView):
    model = Plant
    fields = "__all__"


class PlantDelete(DeleteView):
    model = Plant
    success_url = "/plants/"
