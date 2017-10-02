from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib import admin

# Create your models here.
class Genero (models.Model):
	nomb_genero = models.CharField(max_length=50)
class Comentario(models.Model):
	nomb_comentario = models.CharField(max_length=50)
class Puntuacione(models.Model):
	nomb_puntuacione=models.IntegerField(default=0)
class Creador(models.Model):
	nom_creador=models.CharField(max_length=50)
class Juego (models.Model):
	nombre = models.CharField(max_length=50)
	genero=models.ManyToManyField(Genero)
	comentario=models.ForeignKey(Comentario)
	puntuacione=models.ForeignKey(Puntuacione)
	creador=models.ForeignKey(Creador)

	



	
