from django.db import models

class Membro(models.Model):
    nome = models.CharField(max_length=100)
    nascimento = models.DateField()
    cpf = models.CharField(max_length=14)

    # def __str__ (self):
    #     return self.nome
    