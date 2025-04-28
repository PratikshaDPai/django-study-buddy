from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView


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


def signup(request):
    error_message = ""
    if request.method == "POST":
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in
            login(request, user)
            return redirect("cat-index")
        else:
            error_message = "Invalid sign up - try again"
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {"form": form, "error_message": error_message}
    return render(request, "signup.html", context)
    # Same as:
    # return render(
    #     request,
    #     'signup.html',
    #     {'form': form, 'error_message': error_message}
    # )


class PlantCreate(CreateView):
    model = Plant
    fields = "__all__"

    # This inherited method is called when a
    # valid plant form is being submitted
    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the plant
        # Let the CreateView do its job as usual
        return super().form_valid(form)


class PlantUpdate(UpdateView):
    model = Plant
    fields = "__all__"


class PlantDelete(DeleteView):
    model = Plant
    success_url = "/plants/"


class Home(LoginView):
    template_name = "home.html"
