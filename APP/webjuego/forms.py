from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User 

class RegisterForm(UserCreationForm):
	email = forms.EmailField(label = "Email")
	avatar = forms.ImageField(label = "Avatar",required=False)
	class Meta:
		model = User
		fields = ("username", "first_name", "last_name", "email",'avatar')
