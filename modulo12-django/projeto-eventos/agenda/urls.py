from django.urls import path

from agenda.views import exibir_evento, listar_eventos, evento_participar

urlpatterns = [
    path('', listar_eventos, name="listar_eventos"),
    path('eventos/<int:id>', exibir_evento, name="exibir_evento"),
    path('participar', evento_participar, name="evento_participar")
]
