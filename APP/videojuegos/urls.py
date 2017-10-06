from django.conf.urls import url
from django.contrib import admin

from webjuego import views

from webjuego.views import Juegoslista,JuegosDetail

urlpatterns = [
    # Examples:
    # url(r'^$', 'videojuegos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
    url(r'^$',Juegoslista.as_view(),name='lista-de-juegos'),
    url(r'^juego_list/$',Juegoslista.as_view(),name='lista-de-juegos'),
    url(r'^juego_detalle/(?P<pk>[0-9]+)/$', views.JuegosDetail.as_view(), name='detailles-juego'),
    #url(r'^$',Usuarioscreate.as_view()),
    #url(r'^$',Usuariosupdate.as_view()),
    #url(r'^$',Usuariosdelete.as_view()),
]
