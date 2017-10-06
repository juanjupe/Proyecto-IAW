from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView, UpdateView, DeleteView
from .models import Juego ,Usuario


#from django.forms import ModelForm
# Create your views here.


class Juegoslista(ListView):
	model = Juego
	template_name = "inicio.html"
	context_object_name = 'lista_de_juegos'
	queryset = Juego.objects.all()
	fields = ['nombre','genero','creador','plataforma']
	def __unicode__(self):
		return self.nombre
		
class JuegosDetail(DetailView):
	queryset=Juego.objects.all()
	template_name ="juego_detalle.html"
	def __unicode__(self):
		return self.nombre	
class Usuarioscreate(CreateView):
	model=Usuario
	fields = ['nombre','gmail']

class Usuariosupdate(UpdateView):
	model=Usuario
	fields = ['nombre','gmail']
	
class Usuariosdelete(DeleteView):
	model=Usuario
	
	

