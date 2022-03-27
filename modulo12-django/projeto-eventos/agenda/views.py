from datetime import date
from random import randrange
from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import loader

from agenda.models import Evento

# Create your views here.
def listar_eventos(request):
    eventos = Evento.objects.filter(data__gte=date.today()).order_by('data')
    # get_random =  str(range(100)).zfill(3)
    # get_random = '%03d' % range(100)
    
    for evento in eventos:
      evento.random = '{:0>3}'.format(randrange(1, 120))
    
    get_random = '{:0>3}'.format(randrange(120))
    return render(
        request=request, 
        context={ "eventos": eventos, 'get_random': get_random }, 
        template_name="agenda/listar_eventos.html"
    )

def exibir_evento(request):
    evento = {
        "nome": "Aula teste",
        "categoria": "Categoria teste",
        "local": "Local teste"
    }
    # template = loader.get_template("agenda/exibir_evento.html")
    # rendered_template = template.render(context={ "evento": evento }, request=request)
    
    # return HttpResponse(rendered_template)
    
    return render(
        request=request, 
        context={ "evento": evento }, 
        template_name="agenda/exibir_evento.html"
    )