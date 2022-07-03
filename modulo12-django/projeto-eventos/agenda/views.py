from datetime import date
from random import randrange
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse

from agenda.models import Evento, EventoParticipante, Participante

# Create your views here.
def listar_eventos(request):
    # eventos = Evento.objects.filter(data__gte=date.today()).order_by('data')
    eventos = Evento.objects.exclude(data__lt=date.today()).order_by('data')
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

def exibir_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    participantes = EventoParticipante.objects.filter(evento=evento).count()
    
    return render(
        request=request, 
        context={ "evento": evento, "participantes": participantes }, 
        template_name="agenda/exibir_evento.html"
    )
    
def evento_participar(request):
    evento_id = request.POST.get('evento-id')
    email = request.POST.get('email')
    print(f'evento_id => {evento_id}')
    print(f'email => {email}')
    evento = get_object_or_404(Evento, id=evento_id)
    participante = Participante()
    participante.email = email
    participante.save()
    evento_participante = EventoParticipante()
    evento_participante.evento = evento
    evento_participante.participante = participante
    evento_participante.save()
        
    return HttpResponseRedirect(reverse('exibir_evento', args=(evento_id,)))