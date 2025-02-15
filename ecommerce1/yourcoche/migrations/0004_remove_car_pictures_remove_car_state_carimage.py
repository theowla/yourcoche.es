# Generated by Django 5.1.4 on 2025-01-30 19:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("yourcoche", "0003_car_pictures_alter_car_state_delete_carimage"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="car",
            name="pictures",
        ),
        migrations.RemoveField(
            model_name="car",
            name="state",
        ),
        migrations.CreateModel(
            name="CarImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="car_images/")),
                (
                    "car",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="yourcoche.car",
                    ),
                ),
            ],
        ),
    ]
