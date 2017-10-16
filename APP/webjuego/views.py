from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView, UpdateView, DeleteView
from webjuego.models import Juego ,Usuario

from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
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
	
@login_required(login_url='/ingresar')
def Cerrar(request):
	logout(request)
	return 	HttpResponseRedirect('/')
@login_required(login_url='/ingresar')
def Privado (request):
	usuario=request.user
	return render(request,'privado.html',{'usuario':usuario})
def Ingresar(request):
	if not request.user.is_anonymous():
		return HttpResponseRedirect('/privado')
	if request.method == 'POST':
		formulario = AuthenticationForm(request.POST)
		if formulario.is_valid:
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(password=password,username=username)
			if user is not None:
				if user.is_active:	
					login(request,user)
					return HttpResponseRedirect('/privado')
				else:
					return render('noactivo.html')
			else:
				return render('nousuario.html')
	else:
		formulario=AuthenticationForm()
	return render(request,'ingresar.html',{'formulario':formulario})
	

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
	template_name = "juego_update.html"
	fields = ['nombre','genero','creador','plataforma']
	success_url = reverse_lazy('juego_lista')
	
class JuegoDelete(DeleteView):
	model=Juego
	template_name = "juego_delete.html"
	success_url = reverse_lazy('juego_lista')

	

