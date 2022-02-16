from evento import Evento
from evento_online import EventoOnline

ev1 = Evento("Aula de Python")
ev1.imprime_informacaoes()
ev2 = Evento("Aula de Javascript", "Florianópolis")
ev2.imprime_informacaoes()

print(Evento.calcular_limite_pessoas_por_area(12))

ev1_online = EventoOnline("Live de Python")
ev1_online.imprime_informacaoes()

ev2_online = EventoOnline("Live de Javascript")
ev2_online.imprime_informacaoes()
print(type(ev2_online.to_json()))
print(ev2_online.to_json())