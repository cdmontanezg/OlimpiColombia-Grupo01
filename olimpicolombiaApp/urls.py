from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns =  [
    url(r'deportes$',views.lista_deportes),
    url(r'deportes/(?P<idDeporte>[0-9]+)$',views.deporte),
    url(r'deportes/(?P<idDeporte>[0-9]+)/deportistas$',views.lista_deportistas),
    url(r'deportes/deportistas/(?P<idDeportista>[0-9]+)$',views.deportista),
    url(r'deportistas/(?P<idDeportista>[0-9]+)/eventos$',views.lista_eventos),
    url(r'^s3direct/', include('s3direct.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)