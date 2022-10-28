from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, render
from agenda.models import Agendamento
from agenda.serializers import AgendamentoSerializer

# Create your views here.
@api_view(["GET", "PUT"])
def agendamento_detail(request, id):
    if request.method == "GET":
        agendamento = get_object_or_404(Agendamento, id=id)
        serializer = AgendamentoSerializer(agendamento)
        return JsonResponse(serializer.data)
    
    if request.method == "PUT":
        agendamento = get_object_or_404(Agendamento, id=id)
        serializer = AgendamentoSerializer(agendamento, data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            agendamento.data_horario = validated_data.get("data_horario", agendamento.data_horario)
            agendamento.nome_cliente = validated_data.get("nome_cliente", agendamento.nome_cliente)
            agendamento.email_cliente = validated_data.get("email_cliente", agendamento.email_cliente)
            agendamento.telefone_cliente = validated_data.get("telefone_cliente", agendamento.telefone_cliente)
            agendamento.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

@api_view(http_method_names=["GET", "POST"])
def agendamento_list(request):
    if request.method == "GET":
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
    
    if request.method == "POST":
        # serializa os dados recebidos no request
        serializer = AgendamentoSerializer(data=request.data)
        # verifica se os dados são válidos
        if serializer.is_valid():
            validated_data = serializer.validated_data
            # cria um objeto com os dados validados usando o **kwargs
            # Agendamento.objects.create(**validated_data)
            # ou proderiamos criar da seguinte forma:
            Agendamento.objects.create(
                data_horario=validated_data["data_horario"],
                nome_cliente=validated_data["nome_cliente"],
                email_cliente=validated_data["email_cliente"],
                telefone_cliente=validated_data["telefone_cliente"],
            )
            # persiste os dados no banco de dados
            # serializer.save()
            # retorna o objeto serializado com o status 201 para criado
            return JsonResponse(serializer.data, status=201)
        # se os dados não forem válidos, retorna o erro com o status 400
        return JsonResponse(serializer.errors, status=400)