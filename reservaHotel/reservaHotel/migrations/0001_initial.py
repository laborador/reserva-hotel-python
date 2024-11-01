# Generated by Django 5.0.6 on 2024-10-31 01:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cliente",
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
                ("nombres", models.TextField(max_length=100)),
                ("apellidos", models.TextField(max_length=50)),
                ("direccion", models.TextField(max_length=100)),
                ("telefono", models.TextField(max_length=100)),
                ("email", models.EmailField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Habitacion",
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
                ("numero", models.IntegerField()),
                ("tipo", models.CharField(max_length=50)),
                ("precio", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name="Reserva",
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
                ("fecha_entrada", models.DateField()),
                ("fecha_salida", models.DateField()),
                (
                    "cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="reservaHotel.cliente",
                    ),
                ),
                (
                    "habitacion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="reservaHotel.habitacion",
                    ),
                ),
            ],
        ),
    ]
