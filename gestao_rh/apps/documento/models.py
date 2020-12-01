from django.db import models
from apps.funcionario.models import Funcionario

class Documento(models.Model):
    descricao = models.CharField(max_length=70)

    def __str__(self):
        return self.descricao