# Generated by Django 5.1.6 on 2025-03-01 06:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UserProfile",
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
                ("phone", models.CharField(max_length=20)),
                ("district", models.CharField(max_length=255)),
                ("county", models.CharField(max_length=100)),
                ("sub_county", models.CharField(max_length=100)),
                ("village", models.CharField(max_length=100)),
                ("country", models.CharField(max_length=100)),
                ("zipcode", models.CharField(max_length=10)),
                ("image", models.ImageField(upload_to="profile_image")),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
