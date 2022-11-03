from django.db import models
from django.contrib.auth.models import User
from django.forms import Imagefield
from distutils.command.upload import upload


# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    telefono=models.IntegerField()
    email= models.EmailField()
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Telefono: {self.telefono} - Email: {self.email}"
    
class Mascota(models.Model):
    nombreMascota= models.CharField(max_lenght=50)
    edad= models.IntegerField() 
    raza= models.IntegerField(max_lenght=50)
    motivo= models.IntegerField(max_lenght=50)    
    fecha= models.DateField()
    costo= models.IntegerField()
    
    def __str__(self):
        return f"Nombre: {self.nombreMascota} - Edad: {self.edad} - Raza: {self.raza} - Motivo de Ingreso: {self.motivo} - Fecha: {self.fecha} - Costo: {self.costo} " 
    
 class Cuidador(models.Model):
     Nombrecuid = models.CharField(max_lenght=50)
     apellidocuid = models.CharField(max_lenght=50)
     DNI = models.IntegerField(max_length=8)
     Hogar = models.CharField(max_lenght=50)
     
    def __str__(self):
        return f"Nombre del Cuidador: {self.Nombrecuid} - Apellido del Cuidador: {self.apellidocuid} - Documento de Identidad: {self.DNI} - Hogar de Hospedaje: {self.Hogar} " 
    
     
         
    