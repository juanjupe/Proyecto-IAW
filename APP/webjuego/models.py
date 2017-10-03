from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib import admin

# Create your models here.
class Usuario(models.Model):
	nombre=models.CharField(max_length=50)
	gmail=models.EmailField(max_length=254)
class Genero (models.Model):
	tipo = models.CharField(max_length=50)
class Creador(models.Model):
	patrocinador=models.CharField(max_length=50)
class Juego (models.Model):
	nombre = models.CharField(max_length=50)
	genero=models.ManyToManyField(Genero,default=0)
	creador=models.ForeignKey(Creador,default=0)
class Comentario(models.Model):
	comentario = models.CharField(max_length=50,primary_key=True)
	usuario=models.ManyToManyField(Usuario,default=0)
	juego=models.ForeignKey(Juego,default=0)
class Puntuacione(models.Model):
	valoracion=models.IntegerField(default=0, primary_key=True)
	usuario=models.ManyToManyField(Usuario)
	juego=models.ForeignKey(Juego,default=0)

class Plataforma(models.Model):
	plataforma=models.CharField(max_length=50)
	juego=models.ManyToManyField(Juego,default=0)



	
