# Generated by Django 5.2 on 2025-05-02 05:13

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_watering_options_plant_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Plant',
            new_name='StudyGroup',
        ),
    ]
