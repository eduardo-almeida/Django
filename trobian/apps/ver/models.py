from django.db import models

class Ver(models.Model):
    nome = models.CharField(max_length=100)