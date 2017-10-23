from webjuego.forms import SignUpForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
 
 
class SignUpForm(ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password', 'email', 'first_name', 'last_name']
		widgets = {
		'password': forms.PasswordInput(),
		}

