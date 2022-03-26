from django.contrib import admin

from agenda.models import Categoria, Evento

# Register your models here.
admin.site.register(Evento)
admin.site.register(Categoria)