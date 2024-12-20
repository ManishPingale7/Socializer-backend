# Generated by Django 5.1.4 on 2024-12-11 17:47

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Profile",
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
                ("name", models.CharField(max_length=100)),
                ("photo", models.URLField(max_length=500)),
                ("description", models.TextField()),
                ("address", models.CharField(max_length=255)),
                ("contact_info", models.CharField(max_length=100)),
                ("interests", models.TextField()),
            ],
        ),
    ]
