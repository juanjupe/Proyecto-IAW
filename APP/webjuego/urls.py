from django.conf.urls import  url

from django.contrib import admin

from webjuego import views
from django.core.urlresolvers import reverse_lazy
from webjuego.views import Juegolist,JuegoDetail,JuegoCreate,JuegoUpdate,JuegoDelete,NewUsuario,UsuarioNuevo

urlpatterns = [
    # Examples:
    # url(r'^$', 'videojuegos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
#	url(r'^usuario/nuevo$',views.NewUsuario,name='usuario_nuevo'),
	url(r'^usuario/nuevo$',UsuarioNuevo.as_view(),name='usuario_nuevo'),

	url(r'^ingresar/$',views.Ingresar,name='ingresar'),
	url(r'^privado/$',views.Privado,name='usuario_privado'),
	url(r'^cerrar/$',views.Cerrar,name='cerrar_sesion'),


    url(r'^admin/', admin.site.urls),
    url(r'^$', Juegolist.as_view(),name='juego_lista'),
    url(r'^juego_detalle/(?P<pk>[0-9]+)/$', JuegoDetail.as_view(), name='juego_detalle'),
	url(r'^juego/create/$', JuegoCreate.as_view(), name='juego_create'),
	url(r'^juego/update/(?P<pk>[0-9]+)/$', JuegoUpdate.as_view(), name='juego_update'),
	url(r'^juego/delete/(?P<pk>[0-9]+)/$', JuegoDelete.as_view(), name='juego_delete'),
]
