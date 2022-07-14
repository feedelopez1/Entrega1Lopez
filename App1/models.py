from django.db import models

# Create your models here.


class Cliente(models.Model):
   nombre=models.CharField(max_length=50)
   apellido=models.CharField(max_length=50)
   email=models.EmailField()
   tel=models.IntegerField()

   def __str__(self) -> str:
      return self.nombre




class Empleado(models.Model):
   nombre=models.CharField(max_length=50)
   apellido=models.CharField(max_length=50)
   identificaion=models.IntegerField()
   
   def __str__(self) -> str:
      return self.nombre


class Local(models.Model):
   direccion=models.CharField(max_length=50)
   email=models.EmailField()
   tel=models.IntegerField()

   def __str__(self) -> str:
      return self.nombre



class Producto(models.Model):
   nombre=models.CharField(max_length=50)
   precio=models.FloatField()

   def __str__(self) -> str:
      return self.nombre








