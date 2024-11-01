
from django import forms
from .models import hoteles, Departamento, Municipio,Habitacion, Cliente, Reserva


class ReservaFormulario(forms.ModelForm):
    
    class Meta:
        model = Reserva
        fields = ['habitacion','cliente','fecha_entrada','fecha_salida','precio_total']

    def get_label(self, field):
        if field.name == 'cliente':  
            return self.instance.nombre
        return super().get_label(field)
    
class IngresoCliente (forms.ModelForm):
    class Meta: 
        model = Cliente
        fields = ['nombres' , 'apellidos'  ,  'direccion' ,    'telefono' ,    'email' ]

class IngresoHotel(forms.ModelForm):
    class Meta:
        model = hoteles
        fields = ['nombre_hotel', 'direccion', 'telefono', 'municipio']
        widgets = {
            'municipio': forms.Select(attrs={'class': 'form-control'}),
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['municipio'].queryset = Municipio.objects.all()
        self.fields['municipio'].empty_label = "Selecciona un municipio"

class IngresoHabitacion(forms.ModelForm):
    class Meta:
        model = Habitacion
        fields = ['numero' ,'tipo', 'precio', 'hoteles']


    