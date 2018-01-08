from django.conf.urls import  url

from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from django.views.generic import RedirectView


from webjuego import views
from django.core.urlresolvers import reverse_lazy
from webjuego.views import Juegolist,JuegoDetail,JuegoCreate,JuegoUpdate,JuegoDelete,SignIn,ComentarioForm,hello

urlpatterns = [
    # Examples:
    # url(r'^$', 'videojuegos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
#	url(r'^usuario/nuevo$',views.NewUsuario,name='usuario_nuevo'),

	url(r'^hello/$',views.hello,name='hello'),



	url(r'^usuario/nuevo$',SignIn.as_view(),name='usuario_nuevo'),
	url(r'^comenta/$',ComentarioForm.as_view(),name='comenta'),

	url(r'^ingresar/$',views.Ingresar,name='ingresar'),
	url(r'^privado/$',views.Privado,name='usuario_privado'),
	url(r'^cerrar/$',views.Cerrar,name='cerrar_sesion'),
	url(r'index/$', views.index, name="Index"),
    url(r'^api/$', views.JuegosList.as_view(),name='api'),
	url(r'^$',RedirectView.as_view(url='/TJ/juego_lista')),
	#url(r'^admin/', admin.site.urls,name='administracion'),
	url(r'^juego_lista/$', Juegolist.as_view(),name='juego_lista'),
    url(r'^juego_detalle/(?P<pk>[0-9]+)/$', JuegoDetail.as_view(), name='juego_detalle'),
	url(r'^juego/create/$', JuegoCreate.as_view(), name='juego_create'),
	url(r'^juego/update/(?P<pk>[0-9]+)/$', JuegoUpdate.as_view(), name='juego_update'),
	url(r'^juego/delete/(?P<pk>[0-9]+)/$', JuegoDelete.as_view(), name='juego_delete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

