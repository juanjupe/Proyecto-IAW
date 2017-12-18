from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from django.views.generic import RedirectView


urlpatterns = [
	url(r'TJ/juego_lista/admin/', admin.site.urls,name='administracion'),
    url(r'TJ/', include('webjuego.urls')) , 
	url(r'^$',RedirectView.as_view(url='/TJ/juego_lista')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),


]
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
