from django.shortcuts import render

from .models import hoteles, Habitacion, Cliente, Reserva
import json
from django.http import JsonResponse

from .forms import ReservaFormulario,IngresoCliente,IngresoHotel,IngresoHabitacion

def home(request):
    habitaciones = Habitacion.objects.all()
    return render(request, 'hotel/index.html', {'habitaciones': habitaciones})

def lista_habitaciones(request):
    habitaciones = Habitacion.objects.all()
    return render(request, 'hotel/lista_habitaciones.html', {'habitaciones': habitaciones})
##vistas consultas
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'hotel/lista_clientes.html', {'clientes': clientes})

def lista_hoteles(request):
    lista_hoteles = hoteles.objects.all()
    return render(request, 'hotel/lista_hoteles.html', {'hoteles': lista_hoteles})

def lista_reservaciones(request):
    reservaciones = Reserva.objects.all()
    return render(request, 'hotel/lista_reservaciones.html', {'reservaciones': reservaciones})

##vistas Fomularios
def formulario_reserva(request):    
    if request.method == "POST":
        form = ReservaFormulario(request.POST)       
        if form.is_valid():            
            form.save()
            print('guardado reserva... ok')            
            return render(request, 'hotel/reservaciones.html', {'form': form})    
    else:
        reserva_form = ReservaFormulario()
        return render(request, 'hotel/reservaciones.html', {'form': reserva_form})
    
def formulario_cliente (request):
    if request.method == "POST":
        form = IngresoCliente(request.POST)       
        if form.is_valid():            
            form.save()
            print('guardado cliente... ok')            
            return render(request, 'hotel/clientes.html', {'form': form})    
    else:
        ingreso_cliente_form =  IngresoCliente()
        return render(request, 'hotel/clientes.html', {'form': ingreso_cliente_form})
    
def formulario_hotel(request):
    if request.method == "POST":
        form = IngresoHotel(request.POST)       
        if form.is_valid():            
            form.save()
            print('guardado hotel... ok')            
            return render(request, 'hotel/hotel.html', {'form': form})    
    else:
        ingreso_hotel_form =  IngresoHotel()
        return render(request, 'hotel/hotel.html', {'form': ingreso_hotel_form})

def formulario_habitacion(request):
    if request.method == "POST":
        ingreso_habitacion_form = IngresoHabitacion(request.POST)       
        if ingreso_habitacion_form.is_valid():            
            ingreso_habitacion_form.save()
            print('guardado habitacion... ok')            
            return render(request, 'hotel/habitacion.html', {'form': ingreso_habitacion_form})    
    else:
        ingreso_habitacion_form =  IngresoHabitacion()
        return render(request, 'hotel/habitacion.html', {'form': ingreso_habitacion_form})