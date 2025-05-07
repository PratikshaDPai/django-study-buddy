from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import StudyGroup
from .forms import MessageForm


# Create your views here.


def home(request):
    # Send a simple HTML response
    return render(request, "home.html")


@login_required
def group_index(request):
    groups = StudyGroup.objects.all()
    return render(request, "groups/index.html", {"groups": groups})


def about(request):
    return render(request, "about.html")


@login_required
def group_detail(request, group_id):
    plant = StudyGroup.objects.get(id=group_id)
    message_form = MessageForm()
    return render(
        request, "groups/details.html", {"plant": plant, "message_form": message_form}
    )


@login_required
def add_message(request, group_id):
    # create a ModelForm instance using the data in request.POST
    form = MessageForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the group_id assigned
        new_message = form.save(commit=False)
        new_message.study_group_id = group_id
        new_message.user = request.user
        new_message.save()
    return redirect("plant-detail", group_id=group_id)


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
            return redirect("plant-index")
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


class StudyGroupCreate(LoginRequiredMixin, CreateView):
    model = StudyGroup
    fields = "__all__"

    # This inherited method is called when a
    # valid plant form is being submitted
    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the plant
        # Let the CreateView do its job as usual
        return super().form_valid(form)


class StudyGroupUpdate(LoginRequiredMixin, UpdateView):
    model = StudyGroup
    fields = "__all__"


class StudyGroupDelete(LoginRequiredMixin, DeleteView):
    model = StudyGroup
    success_url = "/groups/"


class Home(LoginView):
    template_name = "home.html"
