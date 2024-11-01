# Generated by Django 5.0.6 on 2024-10-31 02:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "reservaHotel",
            "0002_departamento_pais_reserva_precio_total_municipio_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="habitacion",
            name="hoteles",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="reservaHotel.hoteles",
            ),
            preserve_default=False,
        ),
    ]