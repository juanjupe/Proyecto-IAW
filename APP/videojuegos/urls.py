from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	url(r'^admin/', admin.site.urls),
    url(r'', include('webjuego.urls')) , 
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),


]
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
