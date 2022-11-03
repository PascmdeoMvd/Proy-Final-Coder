from django.shortcuts import render
from django.http import HttpResponse
from .models import Mascota,Persona,Cuidador




# Create your views here.

#----------------------------------------------------------------------#
# Mascota al Hogar

def animal(request):
    return render(request,"AppCoder/animal.html")








#----------------------------------------------------------------------#
# Cliente (Persona)

def persona(request):
    return render(request,"AppCoder/persona.html")



#----------------------------------------------------------------------#
# Cuidador

def cuidador(request):
    return render(request,"AppCoder/cuidador.html")







#----------------------------------------------------------------------#
