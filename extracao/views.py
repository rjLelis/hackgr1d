from django.shortcuts import render
import requests
from .models import Documento

headers = {
    'x-api-key': '88f89251-85d2-4fc5-9a22-97e5d37142b6',
    'endUserId': 'hackagr1d'
}


base_url = 'http://gateway.gr1d.oi/sandbox/compline/v1'

def extrair_rg(request):

    if request.method == 'POST':
        extracao_response = requests.post(f'{base_url}/job/create', headers=headers)
        
        id_job = extracao_response.json().get('idJob')
        tipo = 2

        arquivo = request.FILES

        arquivo = Documento(id_job=id_job, tipo=tipo, arquivo=arquivo)
