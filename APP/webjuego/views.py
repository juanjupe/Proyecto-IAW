from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView, UpdateView, DeleteView
from webjuego.models import Juego ,Usuario

from django.urls import reverse_lazy


from django.views.generic.edit import FormView
#from django.forms import ModelForm
# Create your views here.


class Juegolist(ListView):
	model = Juego
	template_name = "inicio.html"
	

	def __unicode__(self):
		return self.nombre
		
class JuegoDetail(DetailView):
	model=Juego
	template_name ="juego_detalle.html"


class JuegoCreate(CreateView):
	model=Juego
	template_name = "juego_create.html"
	fields = ['nombre','genero','creador','plataforma']	
	success_url = reverse_lazy('juego_lista')
    
	
		
class JuegoUpdate(UpdateView):
	model=Juego
	template_name = "juego_create.html"
	fields = ['nombre','genero','creador','plataforma']
	success_url = reverse_lazy('juego_lista')
	
class JuegoDelete(DeleteView):
	model=Juego
	template_name = "juego_delete.html"
	success_url = reverse_lazy('juego_lista')

	

