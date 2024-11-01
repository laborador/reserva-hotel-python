"""
URL configuration for reservaHotel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import lista_habitaciones, lista_clientes,lista_hoteles, lista_reservaciones, home
from .views import formulario_reserva, formulario_cliente,formulario_hotel, formulario_habitacion


urlpatterns = [
    path("admin/", admin.site.urls),
    path('hotel/lista_habitaciones/', lista_habitaciones, name='lista_habitaciones'),
    path('hotel/reservaciones/',formulario_reserva, name= 'reservaciones'),
    path('hotel/clientes/',formulario_cliente, name= 'clientes'),
    path('hotel/hotel/',formulario_hotel, name='hotel'),
    path('hotel/habitacion/',formulario_habitacion, name='habitacion'),

    path('hotel/lista_clientes/', lista_clientes, name='lista_clientes'),
    path('hotel/lista_hoteles/', lista_hoteles, name='lista_hoteles'),
    path('hotel/lista_reservaciones/', lista_reservaciones, name='lista_reservaciones'),
    path('hotel/index/', home, name='home')
]
