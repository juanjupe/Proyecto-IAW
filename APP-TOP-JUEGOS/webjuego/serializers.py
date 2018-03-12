from rest_framework import serializers
from webjuego.models import Juego


class JuegoSerializer(serializers.ModelSerializer):
	class Meta:
		model=Juego
		fields=('nombre',)
