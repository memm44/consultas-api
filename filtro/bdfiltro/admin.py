from django.contrib import admin
from .models import Libro,Publicador,Autor,Tienda

class AutorReg(admin.ModelAdmin):
    list_display = ["nombre","edad"]

class PublicadorReg(admin.ModelAdmin):
    list_display = ["nombre", "num_premios"]


class LibroReg(admin.ModelAdmin):
    list_display = ["isbn","nombre", "paginas", "precio", "clasificacion","publicadores", "fecha_pub"]
    list_display_links = ["nombre"]
    search_fields = ["nombre"]
class TiendaReg(admin.ModelAdmin):
    list_display = ["nombre"]

admin.site.register(Autor,AutorReg)
admin.site.register(Publicador,PublicadorReg)
admin.site.register(Libro,LibroReg)
admin.site.register(Tienda,TiendaReg)
