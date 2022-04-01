from django.contrib import admin

from agenda.models import Categoria, Evento, EventoParticipante, Participante

# Register your models here.
admin.site.register(Evento)
admin.site.register(Categoria)
admin.site.register(Participante)
admin.site.register(EventoParticipante)