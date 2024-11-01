from django.db import models

# Create your models here.


class Cliente(models.Model):
    
    nombres = models.TextField(max_length=100)
    apellidos = models.TextField(max_length=50)
    direccion = models.TextField(max_length=100)
    telefono = models.TextField(max_length=100)
    email = models.EmailField(max_length=200)



class Pais(models.Model):
    nombre = models.TextField (max_length=100)

class Departamento(models.Model):
    nombre_departamento = models.TextField (max_length=100)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

class Municipio(models.Model):
    nombre_municipio = models.TextField(max_length=100)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

class hoteles(models.Model):
    nombre_hotel = models.TextField(max_length=100)
    direccion = models.TextField(max_length=100)
    telefono  = models.TextField(max_length=100)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)

class Habitacion(models.Model):    
    numero = models.TextField(max_length=200)
    tipo = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    hoteles = models.ForeignKey(hoteles, on_delete=models.CASCADE)

class Reserva(models.Model):
    
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente,  on_delete=models.CASCADE)
    fecha_entrada = models.DateField()
    fecha_salida  = models.DateField()
    precio_total = models.IntegerField(default=0)

class Registro(models.Model):
    correo_electronico = models.EmailField(max_length=200)
    nombre = models.TextField(max_length=200)
    apellido = models.TextField (max_length=200)
    pais_nacimiento = models.TextField(max_length=200)
    departamento_nacimiento = models.TextField(max_length=200)
    municipio_nacimiento = models.TextField (max_length=200)
    telefono= models.TextField(max_length=200)
    contrasena = models.TextField (max_length=20)
    confirma_contrasena= models.TextField(max_length=20)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
