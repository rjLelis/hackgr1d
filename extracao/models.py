from django.db import models

class Documento(models.Model):

    documento_choices = [
        (1, 'CNH'),
        (2, 'RG'),
        (3, 'COMPROVANTE RENDA'),
        (4, 'COMPROVANTE RESIDENCIA'),
        (5, 'CRLV')
    ]

    id_job = models.CharField(max_length=24)

    tipo = models.IntegerField(choices=documento_choices)

    arquivo = models.FileField(upload_to='uploads')
