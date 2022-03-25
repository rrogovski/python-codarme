from django.db import models

# Create your models here.
class Evento:
    def __init__(self, nome, categoria, local=None, link=None):
        self.nome = nome
        self.categoria = categoria
        self.local = local
        self.link = link
        
aula_python = Evento("Aula de Python", "Back-end", "Sinop")
aula_js = Evento("Aula de Javascript", "Fullstack", link="https://rogovski.dev")

eventos = [
    aula_python,
    aula_js
]