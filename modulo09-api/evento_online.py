from evento import Evento

# Herença
class EventoOnline(Evento):
    # Scobreescrevendo o construtor
    # _ para representar que o argumento está sendo ignorado
    def __init__(self, nome, _=""):
        local = f"https://site.com/eventos?id={EventoOnline.id}"
        
        # Como estamos sobreescrevendo o construtor classe pai
        # Devemos chamar o construtor do pai
        super().__init__(nome, local)

    # Sobreescrevendo o método da classe super
    def imprime_informacaoes(self):
        print(f"Nome do evento: {self.nome}")
        print(f"Link para acessar o evento: {self.local}")

    @classmethod
    def criar_evento_online(cls, nome):
        evento = cls(nome, local=f"https://site.com/eventos?id={cls.id}")
        return evento