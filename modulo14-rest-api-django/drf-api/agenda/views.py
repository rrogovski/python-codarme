from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, render
from agenda.models import Agendamento
from agenda.serializers import AgendamentoSerializer

# Create your views here.
@api_view(["GET"])
def agendamento_detail(request, id):
    agendamento = get_object_or_404(Agendamento, id=id)
    serializer = AgendamentoSerializer(agendamento)
    return JsonResponse(serializer.data)

@api_view(http_method_names=["GET"])
def agendamento_list(request):
    # retornar um querySet que é um iterável que representa uma lista de objetos
    # mas não é uma lista
    qs = Agendamento.objects.all()
    # como temos vários objetos, podemos usar nosso serializer para serializar
    # passando o querySet com o parâmetro many=True
    serializer = AgendamentoSerializer(qs, many=True)
    # Por padrão, o JsonResponse serializa apenas do tipo dicionário para JSON
    # mas como estamos serializando um querySet, precisamos passar o parâmetro
    # safe=False para que ele saiba que não é um dicionário
    return JsonResponse(serializer.data, safe=False)