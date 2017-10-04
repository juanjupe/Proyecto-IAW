from django.shortcuts import render
from django.views.generic.list import ListView
from .models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

#from django.forms import ModelForm
# Create your views here.


class Juegos(ListView):
	model = Juego
	template_name = "inicio.html"
	context_object_name = 'lista_de_juegos'
	queryset = Juego.objects.all()
	
	
	
class Usuarioscreate(CreateView):
	model=Usuario
	fields = ['nombre','gmail']

class Usuariosupdate(UpdateView):
	model=Usuario
	fields = ['nombre','gmail']
	
class Usuariosdelete(DeleteView):
	model=Usuario
	success_url = reverse_lazy('Usuario-list')
	

