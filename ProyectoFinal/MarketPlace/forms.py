from django import forms
 
class ProductoFormulario(forms.Form):
    nombre_producto= forms.CharField()
    precio = forms.IntegerField()
    stock =forms.BooleanField()

class VendedorFormulario(forms.Form):
    nombre_apellido= forms.CharField()
    mail= forms.EmailField()
    codigo_interno= forms.IntegerField()

class CategoriaFormulario(forms.Form):
    tipo= forms.CharField()
    estado= forms.CharField()
    tamanio= forms.DecimalField()