from django.urls import path
from .views import *



urlpatterns = [
    path('',inicio,name='inicio'),
    path('cliente/',cliente,name='cliente'),
    path('empleado/',empleado,name='empleado'),
    path('local/',local,name='local'),
    path('producto/',producto,name='producto'),


    path('clienteForm/',clienteForm,name='clienteForm'),
    path('empleadoForm/',empleadoForm,name='empleadoForm'),
    path('localForm/',localForm,name='localForm'),
    path('productoForm/',productoForm,name='productoForm'),

    path('busquedaProducto/',busquedaProducto,name='busquedaProducto'),
    path('buscar/',buscar,name='buscar'),
]
