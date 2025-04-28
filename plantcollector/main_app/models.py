from django.db import models
from django.urls import reverse

# Create your models here.


class Plant(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    # new code below
    def __str__(self):
        return self.name

    # Define a method to get the URL for this particular cat instance
    def get_absolute_url(self):
        # Use the 'reverse' function to dynamically find the URL for viewing this cat's details
        return reverse("plant-detail", kwargs={"plant_id": self.id})


class Watering(models.Model):
    date = models.DateField()

    def __str__(self):
        return f"{self.date}"
