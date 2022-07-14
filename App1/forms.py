from django import forms 




class ClienteForm(forms.Form):
   nombre=forms.CharField(max_length=50)
   apellido=forms.CharField(max_length=50)
   email=forms.EmailField()
   tel=forms.IntegerField()
   

   
class EmpleadoForm(forms.Form):
   nombre=forms.CharField(max_length=50)
   apellido=forms.CharField(max_length=50)
   identificaion=forms.IntegerField()



class LocalForm(forms.Form):
   direccion=forms.CharField(max_length=50)
   email=forms.EmailField()
   tel=forms.IntegerField()



class ProductoForm(forms.Form):
   nombre=forms.CharField(max_length=50)
   precio=forms.FloatField()


class VentaForm(forms.Form):
   articulo=forms.CharField(max_length=50)
   cantidad=forms.IntegerField()
   monto=forms.FloatField()
   
