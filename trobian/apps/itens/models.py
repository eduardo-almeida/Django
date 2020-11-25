from django.db import models
from apps.ver.models import TipoItem

class Item(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    preco = models.IntegerField()
    tipoItem = models.ForeignKey(TipoItem, on_delete=models.PROTECT, null=True, blank=True)
