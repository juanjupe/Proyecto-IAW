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
class Comentario(models.Model):
	comentario = models.CharField(max_length=50)
	usuario=models.OneToOneField(Usuario, primary_key=True,default=0)
class Puntuacione(models.Model):
	valoracion=models.IntegerField(default=0)
	usuario=models.OneToOneField(Usuario, primary_key=True)
class Creador(models.Model):
	patrocinador=models.CharField(max_length=50)
class Juego (models.Model):
	nombre = models.CharField(max_length=50)
	genero=models.ManyToManyField(Genero,default=0)
	comentario=models.ForeignKey(Comentario,default=0)
	puntuacione=models.ForeignKey(Puntuacione,default=0)
	creador=models.ForeignKey(Creador,default=0)
	




	
