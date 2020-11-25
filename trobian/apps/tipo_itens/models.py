from django.db import models

class TipoItem(models.Model):
    nome = models.CharField(max_length=100)