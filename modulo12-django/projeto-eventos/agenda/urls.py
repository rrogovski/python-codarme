from django.urls import path

from agenda.views import exibir_evento, listar_eventos

urlpatterns = [
    path('', listar_eventos),
    path('eventos/<int:id>', exibir_evento)
]
