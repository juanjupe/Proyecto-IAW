from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User 
from .models import Comentario


class RegisterForm(UserCreationForm):
	email = forms.EmailField(label = "Email")
	avatar = forms.ImageField(label = "Avatar",required=False)
	class Meta:
		model = User
		fields = ("username", "first_name", "last_name", "email",'avatar')


class ComentarioForm(forms.ModelForm):
	comentario = forms.CharField(label = 'comentario')
	class Meta:
		model = Comentario
		fields = ('comentario',)
