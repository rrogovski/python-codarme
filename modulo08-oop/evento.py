class Evento:
    id = 1

    def __init__(self, nome, local=""):
        self.nome = nome
        self.local = local
        # setando o atributo de instância com base no valor atual do atributo de classe
        self.id = Evento.id

        # incementendo o atributo de classe que é compartilhado por todas as instâncias
        Evento.id += 1

    def imprime_informacaoes(self):
        print(f"Nome do evento: {self.nome}")
        print(f"Local do evento: {self.local}")

    @classmethod
    def criar_evento_online(cls, nome):
        evento = cls(nome, local=f"https://site.com/eventos?id={cls.id}")
        return evento

    @staticmethod
    def calcular_limite_pessoas_por_area(area_m2):
        if 5 <=area_m2 < 10:
            return 5
        elif 10 <= area_m2 < 20:
            return 15
        elif area_m2 >= 20:
            return 30
        else:
            return 0

# ev1 = Evento("Aula de Python")
# ev2 = Evento("Aula de Javascript", "Florianópolis")

print(Evento.calcular_limite_pessoas_por_area(12))

ev1_online = Evento.criar_evento_online("Live de Python")
ev1_online.imprime_informacaoes()

ev2_online = Evento.criar_evento_online("Live de Javascript")
ev2_online.imprime_informacaoes()
