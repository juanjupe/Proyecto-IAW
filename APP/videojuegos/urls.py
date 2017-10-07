from django.conf.urls import url
from django.contrib import admin

from webjuego import views

from webjuego.views import Juegoslista,JuegosDetail,UsuarioList,UsuarioDetail,UsuarioCreation,UsuarioUpdate,UsuarioDelete

urlpatterns = [
    # Examples:
    # url(r'^$', 'videojuegos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
    url(r'^$',Juegoslista.as_view(),name='pagina-principal'),
    url(r'^juego_list/$',Juegoslista.as_view(),name='lista-de-juegos'),
    url(r'^juego_detalle/(?P<pk>[0-9]+)/$', views.JuegosDetail.as_view(), name='detalles-juego'),
	
	url(r'^$', views.UsuarioList.as_view(), name='list'),
	url(r'^(?P<pk>[0-9]+)/$', views.UsuarioDetail.as_view(), name='detail'),
	url(r'^nuevo/(?P<pk>[0-9]+)/$', views.UsuarioCreation.as_view(), name='new'),
	url(r'^editar/(?P<pk>[0-9]+)/$', views.UsuarioUpdate.as_view(), name='edit'),
	url(r'^borrar/(?P<pk>[0-9]+)/$', views.UsuarioDelete.as_view(), name='delete'),

    #url(r'^$',Usuarioscreate.as_view()),
    #url(r'^$',Usuariosupdate.as_view()),
    #url(r'^$',Usuariosdelete.as_view()),
]
