from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView, UpdateView, DeleteView 

from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http.response import HttpResponseRedirect
from django.views.generic import TemplateView
from webjuego.forms import RegisterForm
from .forms import ComentarioForm
from django.shortcuts import redirect

from webjuego.serializers import JuegoSerializer
from webjuego.models import Juego ,Usuario , Comentario,User
from rest_framework import generics


def index(request):
	if request.user.is_authenticated and request.user != "AnonymousUser":

		return render(request, "info.html")
	else:
		return render(request, "info.html")


class JuegosList(generics.ListCreateAPIView):
    queryset = Juego.objects.all()
    serializer_class = JuegoSerializer


class ComentarioForm(FormView):
	template_name = 'comentarioform.html'
	form_class = ComentarioForm
	success_url = reverse_lazy('juego_lista')
	
	def form_valid(self, form):
		user=form.save.unicode()
		usuario=Usuario.unicode()
		user.usuario.save.unicode()
		return super(ComentarioForm, self).form_valid(form)
		
	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.comenteraio=form.cleaned_data['comentario']
		self.object.save()
		return HttpResponseRedirect(self.get_success_url())



	
@login_required(login_url='/ingresar')
def Cerrar(request):
	logout(request)
	return 	HttpResponseRedirect('/')
	
@login_required(login_url='/ingresar')
def Privado (request):
	usuario=request.user
	return render(request,'privado.html',{'usuario':usuario})
	
from django.contrib import messages
	
def Ingresar(request):
	if not request.user.is_anonymous():
		return HttpResponseRedirect('privado')
	if request.method == 'POST':
		formulario = AuthenticationForm(request.POST)
		if formulario.is_valid:
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(password=password,username=username)
			if user is not None:
				if user.is_active:	
					login(request,user)
					return HttpResponseRedirect('/TJ/privado')
				else:
					
					return render(request,'noactivo.html')
			else:
				storage = messages.get_messages(request)
				storage.used=True
				messages.add_message(request, messages.INFO, "El usuario "+str(username)+" no existe.")				
				return render(request,'nousuario.html')
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
	queryset=Juego.objects.all()
	def __unicode__(self):
		return self.nombre




class JuegoCreate(CreateView):
	select_related = ['user']
	model=Juego
	template_name = "juego_create.html"
	fields = ['nombre','genero','creador','plataforma']	
	success_url = reverse_lazy('juego_lista')
	
	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(JuegoCreate, self).dispatch(*args, **kwargs)

		
class JuegoUpdate(UpdateView):
	model=Juego
	template_name = "juego_update.html"
	fields = ['nombre','genero','creador','plataforma']
	success_url = reverse_lazy('juego_lista')
	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(JuegoUpdate, self).dispatch(*args, **kwargs)
		
			
class JuegoDelete(DeleteView):
	model=Juego
	template_name = "juego_delete.html"
	success_url = reverse_lazy('juego_lista')
	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(JuegoDelete, self).dispatch(*args, **kwargs)
		
class SignIn(FormView):
	template_name = 'nuevousuario.html'
	form_class = RegisterForm
	success_url = reverse_lazy('juego_lista')

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.user = self.request.user
		self.object.save()
		return HttpResponseRedirect(self.get_success_url())
	def form_valid(self, form):
		user=form.save()
		usuario=Usuario()
		usuario.user=user
		usuario.avatar=form.cleaned_data['avatar']
		usuario.save()
		return super(SignIn, self).form_valid(form)
