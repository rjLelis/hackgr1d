from django.db import models

class Equipamento(models.Model):

    descricao = models.CharField(max_length=100, null=False)
