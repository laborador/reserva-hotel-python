# Generated by Django 5.0.6 on 2024-10-31 02:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reservaHotel", "0003_habitacion_hoteles"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habitacion",
            name="numero",
            field=models.TextField(max_length=200),
        ),
    ]
