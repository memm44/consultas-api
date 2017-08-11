from django.shortcuts import render
from django.views.generic import CreateView,TemplateView,View,ListView
from .models import Autor,Publicador,Tienda,Libro
from django.db.models import Avg,Max,Min,Count,Sum

class Inicio(View):
    template_name = "index.html"
    consulta = Publicador.objects.annotate(x=Count("libro")).filter(x__lte=2)


    def get(self,request,**kwargs):
        consulta=self.consulta
        context= {
            "consulta":consulta
        }
        print(context)
        return render(request, self.template_name,context)


'''
cual es el publicador que tiene mas libros y cuantos son 			luis:6
>>> Publicador.objects.annotate(n=Count("libro")).order_by("-n")[:1]  a[0].n 

cual es el libro mejor clasificado 
>>> Libro.objects.annotate(n=Max("clasificacion")).order_by("-n")[:1]  

>>> Libro.objects.annotate(n=Max("clasificacion")).order_by("-n")[0]  
por indice en vez de Slice, solo para cuando se trata de un objeto ... [1] seria el segundo mejor clasificado

cual de los libros de jquery es el peor rankeado 
>>> Libro.objects.filter(nombre__startswith="Jquery").annotate(x=Min("clasificacion")).order_by("x")[:1]

cuantos publicadores tienen menos de dos libros  
>>> Publicador.objects.annotate(x=Count("libro")).filter(x__lt=2)

cual es el libro mas barato 
>>> Libro.objects.annotate(x=Min("precio")).order_by("x")[:1]

cual es el libro mas caro 
>>> Libro.objects.annotate(x=Max("precio")).order_by("x")[:1]

cual tienda tiene mas libros 
>>> Tienda.objects.annotate(n=Count("libros")).order_by("-n")[:1]

cual es el precio total de todos los libros jquery
>>> Libro.objects.filter(nombre__startswith="Jquery").aggregate(n=Sum("precio"))

cual es el peor publicador
>>> Publicador.objects.annotate(n=Min("num_premios")).order_by("n")[:1]

que publicador ha ganado mas premios
>>> Publicador.objects.annotate(n=Max("num_premios")).order_by("-n")[:1]

>>> Publicador.objects.annotate(x=Count("libro")).filter(libro__lt=2).order_by("x")
'''