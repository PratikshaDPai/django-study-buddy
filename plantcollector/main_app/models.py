from django.db import models

# Create your models here.


class Plant:
    def __init__(self, name, species, description):
        self.name = name
        self.species = species
        self.description = description


# List of Plant instances
plants = [
    Plant("Jerry", "Money Plant", "Durable"),
    Plant("Figgy", "Fiddle Lead Fig", "Drama queen"),
]
