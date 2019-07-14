from django.db.models.signals import post_save
from django.dispatch import receiver
from extracao.models import Documento
import requests

@receiver(post_save, sender=Documento)
def create_planilha(sender, instance, created, **kwargs):
    if created:
        headers = {
            'x-api-key': 'b7483bb4-f7f9-4521-a047-223fc550a1cb',
            'endUserId': 'hackagr1d'
        }
        files = {'File': open(instance.arquivo.paht)}
        requests.put(f'http://gateway.gr1d.oi/sandbox/compline/v1/job/upload/{instance.id_job}/{instance.tipo}', files=files, headers=headers)