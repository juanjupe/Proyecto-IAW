from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

	
class Usuario(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE,unique=True)
	avatar = models.ImageField()

	def __str__(self):
		return str(self.user)


    
class Genero (models.Model):
	tipo = models.CharField(max_length=50)
	
	def __str__(self):
		return self.tipo

	
class Creador(models.Model):
	patrocinador=models.CharField(max_length=50)

	def __str__(self):
		return self.patrocinador	
	
	
class Plataforma(models.Model):
	plataforma=models.CharField(max_length=50)

	def __str__(self):
		return self.plataforma	
	
	
class Juego (models.Model):
	nombre = models.CharField(max_length=50)
	genero=models.ManyToManyField(Genero,default=0)
	creador=models.ForeignKey(Creador,default=0)
	plataforma=models.ManyToManyField(Plataforma,default=0)

	def __unicode__(self):
		return self.nombre
		
	def __str__(self):
		return self.nombre
		
	def get_absolute_url(self):
		return reverse('juego-detail', kwargs={'pk': self.pk})
		
class Comentario(models.Model):
	comentario = models.CharField(max_length=50,primary_key=True)
	usuario=models.ManyToManyField(Usuario,default=0)
	juego=models.ForeignKey(Juego,default=0)
	
	
	
class Puntuacione(models.Model):
	valoracion=models.IntegerField(default=0, primary_key=True)
	usuario=models.ManyToManyField(Usuario)
	juego=models.ForeignKey(Juego,default=0)




