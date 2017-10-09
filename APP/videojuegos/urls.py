<<<<<<< HEAD
from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('webjuego.urls')) ,   

=======
from django.conf.urls import url
from django.contrib import admin

from webjuego import views

from webjuego.views import Juegolist,JuegoDetail,JuegoCreate,JuegoUpdate,JuegoDelete

urlpatterns = [
    # Examples:
    # url(r'^$', 'videojuegos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
    url(r'^$', views.Juegolist.as_view(),name='juego_list'),
    url(r'^juego_detalle/(?P<pk>[0-9]+)/$', views.JuegoDetail.as_view(), name='inicio_list'),
	url(r'^juego_nuevo/(?P<pk>[0-9]+)/$', views.JuegoCreate.as_view(), name='juego_new'),
	url(r'^juego_editar/(?P<pk>[0-9]+)/$', views.JuegoUpdate.as_view(), name='juego_edit'),
	url(r'^juego_borrar/(?P<pk>[0-9]+)/$', views.JuegoDelete.as_view(), name='juego_delete'),
>>>>>>> 1ac5c16f0466e5997e3bdbe7ca1aa7793e3a9d05
]
