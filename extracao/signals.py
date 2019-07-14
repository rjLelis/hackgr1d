from django.db.models.signals import post_save
from django.dispatch import receiver
from extracao.models import Documento
import requests

@receiver(post_save, sender=Documento)
def create_planilha(sender, instance, created, **kwargs):
    if created:
        headers = {
            'x-api-key': '88f89251-85d2-4fc5-9a22-97e5d37142b6',
            'endUserId': 'hackagr1d'
        }
        files = {'File': open(instance.arquivo.path)}
        requests.put(f'http://gateway.gr1d.oi/sandbox/compline/v1/job/upload/{instance.id_job}/{instance.tipo}', files=files, headers=headers)