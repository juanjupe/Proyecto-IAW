from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView, UpdateView, DeleteView
from webjuego.models import Juego ,Usuario

from django.urls import reverse_lazy

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
	
	
		
class UsuarioList(ListView):
    model = Usuario
    template_name = "usuario_list.html"
    success_url = reverse_lazy('webjuego:list')

class UsuarioDetail(DetailView):
    model = Usuario
		
class UsuarioCreation(CreateView):
	model=Usuario
	fields = ['nombre','gmail']
	template_name ="usuario.html"
	success_url = reverse_lazy('webjuego:list')
	fields = ['nombre','gmail']	
		
class UsuarioUpdate(UpdateView):
	model=Usuario
	fields = ['nombre','gmail']
	success_url = reverse_lazy('webjuego:list')
	
class UsuarioDelete(DeleteView):
	model=Usuario
	success_url = reverse_lazy('webjuego:list')
	

