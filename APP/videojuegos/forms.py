from django import forms

<<<<<<< HEAD
class ContactForm(forms.Form):
	name = forms.CharField()
	message = forms.CharField(widget=forms.Textarea)
	def send_email(self):
		pass
=======
from .models import Raza,Perro,Propiedade,Usuario
class UsuarioForm(forms.ModelForm):
	class Meta:
		model=Usuario
		fields=['nombre','gmail']
>>>>>>> 1ac5c16f0466e5997e3bdbe7ca1aa7793e3a9d05
