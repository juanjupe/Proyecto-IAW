from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView, UpdateView, DeleteView
from webjuego.models import Juego ,Usuario

from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http.response import HttpResponseRedirect


def NewUsuario(request):
	if request.method == 'POST':
		formulario = UserCreationForm(request.POST)  
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario=UserCreationForm()
	return render(request,'nuevousuario.html',{'formulario':formulario})



class Juegolist(ListView):
	model = Juego
	template_name = "inicio.html"
	

	def __unicode__(self):
		return self.nombre
		
class JuegoDetail(DetailView):
	model=Juego
	template_name ="juego_detalle.html"
	def __unicode__(self):
		return self.nombre


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

	

