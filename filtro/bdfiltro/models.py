from django.db import models

class Autor(models.Model):
    nombre= models.CharField(max_length=100)
    edad= models.IntegerField()
    amigos= models.ManyToManyField("self",blank=True)
    def __str__(self):
        return self.nombre

class Publicador(models.Model):
    nombre=models.CharField(max_length=300)
    num_premios=models.IntegerField()
    def __str__(self):
        return self.nombre

class Libro(models.Model):
    isbn= models.CharField(max_length=9)
    nombre= models.CharField(max_length=100)
    paginas= models.IntegerField()
    precio= models.DecimalField(max_digits=10,decimal_places=2)
    clasificacion= models.FloatField()
    autores= models.ManyToManyField(Autor)
    publicadores= models.ForeignKey(Publicador)
    fecha_pub= models.DateField()
    def __str__(self):
        return self.nombre

class Tienda(models.Model):
    nombre= models.CharField(max_length=100)
    libros= models.ManyToManyField(Libro)
    def __str__(self):
        return self.nombre
