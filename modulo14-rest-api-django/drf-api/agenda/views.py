from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from agenda.models import Agendamento
from agenda.serializers import AgendamentoSerializer

# Create your views here.
def agendamento_detail(request, id):
    agendamento = get_object_or_404(Agendamento, id=id)
    serializer = AgendamentoSerializer(agendamento)
    return JsonResponse(serializer.data)