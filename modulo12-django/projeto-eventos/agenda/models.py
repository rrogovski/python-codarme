from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=256, unique=True)
    
    def __str__(self):
        return f"{self.id} - {self.nome}"

class Participante(models.Model):
    email = models.CharField(max_length=256)
    
    def __str__(self):
        return f"{self.id} - {self.email}" 
class Evento(models.Model):
    nome = models.CharField(max_length=256)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    local = models.CharField(max_length=256, blank=True)
    link = models.CharField(max_length=256, blank=True)
    data = models.DateField(null=True)
    participantes = models.ManyToManyField(Participante, through='EventoParticipante')
    
    def total_participantes(self):
        self.participantes.count()
    
    def __str__(self):
        return f"{self.id} - {self.nome}"    
class EventoParticipante(models.Model):
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.id} - {self.evento.nome} | {self.participante.email}"
