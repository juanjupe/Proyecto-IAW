from rest_framework import serializers
from webjuego.models import Juego


class JuegoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)	
	nombre = serializers.CharField(max_length=50)
	genero=serializers.ManyToManyField(Genero,default=0)
	creador=serializers.ForeignKey(Creador,default=0)
	plataforma=serializers.ManyToManyField(Plataforma,default=0)
	

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Juego.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.nombre = validated_data.get('title', instance.title)
        instance.genero = validated_data.get('code', instance.code)
        instance.creador = validated_data.get('linenos', instance.linenos)
        instance.plataforma = validated_data.get('language', instance.language)
        instance.save()
        return instance
