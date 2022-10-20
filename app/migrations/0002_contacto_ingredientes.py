# Generated by Django 4.1.1 on 2022-10-18 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contacto",
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
                ("nombre", models.CharField(max_length=50)),
                ("correo", models.EmailField(max_length=254)),
                (
                    "tipo_consulta",
                    models.IntegerField(
                        choices=[
                            [0, "Consulta"],
                            [1, "Reclamo"],
                            [2, "Sugerencia"],
                            [3, "Felicitaciones"],
                        ]
                    ),
                ),
                ("mensaje", models.TextField()),
                ("avisos", models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name="Ingredientes",
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
                ("nombre", models.CharField(max_length=50)),
                ("cantidad", models.IntegerField()),
            ],
        ),
    ]