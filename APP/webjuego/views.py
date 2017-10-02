from django.shortcuts import render
from django.views.generic.list import ListView
from .models import *

#from django.forms import ModelForm
# Create your views here.


class Juegos(ListView):
	model = Juego
	template_name = "inicio.html"
