from django import forms

from .models import Raza,Perro,Propiedade,Usuario
class UsuarioForm(forms.ModelForm):
	class Meta:
		model=Usuario
		fields=['nombre','gmail']
