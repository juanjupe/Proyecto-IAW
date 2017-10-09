from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView, UpdateView, DeleteView
from webjuego.models import Juego ,Usuario

from django.urls import reverse_lazy

<<<<<<< HEAD
from videojuegos.forms import ContactForm
from django.views.generic.edit import FormView
=======
>>>>>>> 1ac5c16f0466e5997e3bdbe7ca1aa7793e3a9d05
#from django.forms import ModelForm
# Create your views here.


class Juegolist(ListView):
	model = Juego
<<<<<<< HEAD
	template_name = "inicio.html"
	

=======
	#success_url = reverse_lazy('juego_list')
	template_name = "inicio.html"
	#context_object_name = 'lista_de_juegos'
	#queryset = Juego.objects.all()
	#fields = ['nombre','genero','creador','plataforma']
>>>>>>> 1ac5c16f0466e5997e3bdbe7ca1aa7793e3a9d05
	def __unicode__(self):
		return self.nombre
		
class JuegoDetail(DetailView):
<<<<<<< HEAD
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

=======
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
>>>>>>> 1ac5c16f0466e5997e3bdbe7ca1aa7793e3a9d05
	

