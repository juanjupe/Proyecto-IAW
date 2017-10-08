from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView, UpdateView, DeleteView
from webjuego.models import Juego ,Usuario

from django.urls import reverse_lazy

#from django.forms import ModelForm
# Create your views here.


class Juegolist(ListView):
	model = Juego
	#success_url = reverse_lazy('juego_list')
	template_name = "inicio.html"
	#context_object_name = 'lista_de_juegos'
	#queryset = Juego.objects.all()
	#fields = ['nombre','genero','creador','plataforma']
	def __unicode__(self):
		return self.nombre
		
class JuegoDetail(DetailView):
	queryset=Juego.objects.all()
	template_name ="juego_detalle.html"
	def __unicode__(self):
		return self.nombre	
	

class JuegoCreate(CreateView):
	model=Usuario
	success_url = reverse_lazy('inicio')
	fields = ['nombre','gmail']	
		
class JuegoUpdate(UpdateView):
	model=Usuario
	fields = ['nombre','gmail']
	success_url = reverse_lazy('inicio')
	
class JuegoDelete(DeleteView):
	model=Usuario
	success_url = reverse_lazy('inicio')
	

