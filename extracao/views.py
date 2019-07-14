from django.shortcuts import render
import requests
from .models import Documento

headers = {
    'x-api-key': 'b7483bb4-f7f9-4521-a047-223fc550a1cb',
    'endUserId': 'hackagr1d'
}


base_url = 'http://gateway.gr1d.oi/sandbox/compline/v1'

def extrair_rg(request):

    if request.method == 'POST':
        extracao_response = requests.post(f'{base_url}/job/create', headers=headers)
        
        id_job = rg_response.json().get('idJob')
        tipo = 2

        arquivo = request.FILES

        arquivo = Documento(id_job=id_job, tipo=tipo, arquivo=arquivo)
