from django.shortcuts import render
from .models import Habitacion
from .models import hoteles, Habitacion
import json
from django.http import JsonResponse
from .forms import ReservaFormulario

def lista_habitaciones(request):
    habitaciones = Habitacion.objects.all()
    return render(request, 'hotel/lista_habitaciones.html', {'habitaciones': habitaciones})



def formulario_reserva(request):
    form = ReservaFormulario()
    return render(request, 'hotel/lista_habitaciones.html', {'form': form})

