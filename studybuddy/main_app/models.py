from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class StudyGroup(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    # Admin user (group owner)
    admin = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="admin_study_groups"
    )

    # Members of the study group
    members = models.ManyToManyField(User, related_name="study_groups")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("plant-detail", kwargs={"plant_id": self.id})


class Message(models.Model):
    date = models.DateField()
    study_group = models.ForeignKey(StudyGroup, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date} - {self.user.username}"

    class Meta:
        ordering = ["-date"]
