from django.db import models
from django.contrib.auth.models import User
from apps.departamento.models import Departamento


class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    departamentos = models.ManyToManyField(Departamento)

    def __str__(self):
        return self.nome