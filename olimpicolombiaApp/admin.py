from django.contrib import admin
from .models import Deporte
from .models import Deportista
from .models import Evento

# Register your models here.
admin.site.register(Deporte)
admin.site.register(Deportista)
admin.site.register(Evento)
