from django.conf.urls import url
from django.contrib import admin

from webjuego import views
<<<<<<< HEAD
from django.core.urlresolvers import reverse_lazy
from webjuego.views import Juegolist,JuegoDetail,JuegoCreate,JuegoUpdate,JuegoDelete
=======

from webjuego.views import Juegoslista,JuegosDetail,JuegoCreation,JuegoUpdate,JuegoDelete
>>>>>>> 1ac5c16f0466e5997e3bdbe7ca1aa7793e3a9d05

urlpatterns = [
    # Examples:
    # url(r'^$', 'videojuegos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

<<<<<<< HEAD
    url(r'^admin/', admin.site.urls),
    url(r'^$', Juegolist.as_view(),name='juego_lista'),
    url(r'^juego_detalle/(?P<pk>[0-9]+)/$', JuegoDetail.as_view(), name='juego_detalle'),
	url(r'^juego/create/$', JuegoCreate.as_view(), name='juego_create'),
	url(r'^juego/update/(?P<pk>[0-9]+)/$', JuegoUpdate.as_view(), name='juego_update'),
	url(r'^juego/delete/(?P<pk>[0-9]+)/$', JuegoDelete.as_view(), name='juego_delete'),
]
=======
    url(r'^webjuego/', include ('webjuego.urls')),
]

>>>>>>> 1ac5c16f0466e5997e3bdbe7ca1aa7793e3a9d05
