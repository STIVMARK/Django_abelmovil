from django import forms
from .models import *


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['Nombre','Apellido','Cedula','edad','Direccion','mail']


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields= ['Nombre','Apellido','Cedula','edad','Direccion','mail']


class MantenimientoForm(forms.ModelForm):
    class Meta:
        model = Mantenimiento
        fields=['Codigo', 'dispositivo','sistema_Operativo','descripcion' ,'Precio']


class NotaVentaForm(forms.ModelForm):
    class Meta:
        model  = Nota_Venta
        fields = ['Codigo','Cliente','Direccion','fecha']
        widgets = {'fecha': forms.DateInput(format=('%m/%d/%Y'),attrs={'type':'date' })}



class DetalleVentaForm(forms.ModelForm):
    class Meta:
        model = Detalle_Nota_Venta
        fields = ['codigo','cantidad','mantenimiento','valor_Unitario','valor_total']

class FacturaForm(forms.ModelForm):
    class Meta:
        model= Factura
        fields = ['encabezado','detalle']























































