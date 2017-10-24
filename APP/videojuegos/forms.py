from django import forms
from django.contrib.auth.forms import UserCreationForm
     
class UserFormss(UserCreationForm):
	email = forms.EmailField(label = "Email")
	avatar = forms.ImageField(label = "avatar")
	
	class Meta:
		model = User
		fields = ( "email","avatar" )
