from django.conf.urls import url,include
from django.contrib import admin
from webjuego.views import Usuarioscreate, Usuariosupdate, Usuariosdelete

from webjuego.views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'videojuegos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',Juegos.as_view()),
    url(r'^$',Usuarioscreate.as_view()),
    url(r'^$',Usuariosupdate.as_view()),
    url(r'^$',Usuariosdelete.as_view()),
]
