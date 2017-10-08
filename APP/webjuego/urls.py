from django.conf.urls import url
from django.contrib import admin

from webjuego import views

from webjuego.views import Juegoslista,JuegosDetail,JuegoCreation,JuegoUpdate,JuegoDelete

urlpatterns = [
    # Examples:
    # url(r'^$', 'videojuegos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^webjuego/', include ('webjuego.urls')),
]

