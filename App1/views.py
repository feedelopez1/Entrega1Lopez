from django.shortcuts import render
from django.http import HttpResponse
from App1.models import *
from App1.forms import *

# Create your views here.

def inicio(request):
   return render(request,'App1/inicio.html')



def cliente(request):
   return render(request,'App1/cliente.html')

def clienteForm(request):
   if(request.method=='POST'):
      form=ClienteForm(request.POST)
      if form.is_valid():
         info=form.cleaned_data
         nombre=info['nombre']
         apellido=info['apellido']
         email=info['email']
         tel=info['tel']
         cliente=Cliente(nombre=nombre,apellido=apellido,email=email,tel=tel)
         cliente.save()
         return render(request,'App1/inicio.html')
   else:
      form= ClienteForm()
   return render(request,'App1/clienteFormulario.html',{'form':form})


def empleado(request):
   return render(request,'App1/empleado.html')

def empleadoForm(request):
   if request.method=='POST':
      form=EmpleadoForm(request.POST)
      if form.is_valid():
         info=form.cleaned_data
         nombre=info['nombre']
         apellido=info['apellido']
         identificacion=info['identificacion']
         empleado=Empleado(nombre=nombre,apellido=apellido,identificacion=identificacion)
         empleado.save()
         return render(request,'App1/inicio.html')
   else:
      form= EmpleadoForm()
   return render(request,'App1/empleadoFormulario.html',{'form':form})





def local(request):
   return render(request,'App1/local.html')
   

def localForm(request):
   if(request.method=='POST'):
      form=LocalForm(request.POST)
      if form.is_valid():
         info=form.cleaned_data
         direccion=info['direccion']
         email=info['email']
         tel=info['tel']
         local=Local(direccion=direccion,email=email,tel=tel)
         local.save()
         return render(request,'App1/localFormulario.html')
   else:
      form= LocalForm()
   return render(request,'App1/localFormulario.html',{'form':form})


def busquedaProducto(request):
   
   return render(request, 'App1/busquedaProducto.html')

def buscar(request):
   if request.get('nombre'):
      nombre=request.get('nombre')
      nombre=Producto.objects.filter(nombre=nombre)

      return render(request,'App1/resultado.html',{'nombre':nombre})
   else:
      return render(request, 'App1/busquedaProducto.html',{'error':'No se ingreso ningun producto'})



def producto(request):
   return render(request,'App1/producto.html')

def productoForm(request):
   if(request.method=='POST'):
      form=ProductoForm(request.POST)
      if form.is_valid():
         info=form.cleaned_data
         nombre=info['nombre']
         precio=info['precio']
         producto=Producto(nombre=nombre,precio=precio)
         producto.save()
         return render(request,'App1/productoFormulario.html')
   else:
      form= ProductoForm()
   return render(request,'App1/productoFormulario.html',{'form':form})


