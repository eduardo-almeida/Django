from django.db import models
# pylint: disable=import-error
from cpf_field.models import CPFField

#from cep.widgets import CEPInput


class Visitante(models.Model):
    nome = models.CharField(max_length=150, help_text="Nome do Visitante")
    cpf = CPFField('cpf')
    #endereco
    #cep
    #telefone
    #email