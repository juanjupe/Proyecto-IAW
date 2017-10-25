from django.contrib import admin
from .models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# Register your models here.

admin.site.register(Genero)
admin.site.register(Comentario)
admin.site.register(Juego)
admin.site.register(Puntuacione)
admin.site.register(Creador)
admin.site.register(Usuario)
admin.site.register(Plataforma)




class UsuarioInline(admin.StackedInline):
	model= Usuario
	can_delete=False
	verbose_name_plurar='usuario'
	fk_name='user'
  	
class CustomUserAdmin(UserAdmin):
	inlines=(UsuarioInline,)
	def get_inline_instances(self, request, obj=None):
		if not obj:
			return list()
		return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User , CustomUserAdmin)
