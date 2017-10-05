from django import forms
from webjuego.models import Usuario


class UsuarioForm(forms.ModelForm):
	class Meta:
		model=Usuario
		fields=[
		'nombre',
		'gmail']
