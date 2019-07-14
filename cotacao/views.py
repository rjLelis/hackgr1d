from django.shortcuts import render, redirect
from datetime import datetime
import requests
import json

headers = {
    'x-api-key': 'b7483bb4-f7f9-4521-a047-223fc550a1cb'
}

base_url = 'http://gateway.gr1d.io/sandbox/travelace/v1'

def sucesso(request):
    return render(request, 'cotacao/sucesso.html')


def erro(request):
    return render(request, 'cotacao/erro.html')


def home(request):
    
    if request.method == 'POST':

        destinos = request.POST.get('destinos').split(',')
        qtd_mais_70_anos = int(request.POST.get('maisDe70'))
        passageiro = {}
        passageiros = []
        ano_mais_70 = datetime.now().year - 70
        for _ in range(qtd_mais_70_anos):
            passageiro['nome'] = 'Desconhecido'
            passageiro['dataNascimento'] = f'{ano_mais_70}-01-01'
            passageiros.append(passageiro)

        qtd_menos_70_anos = int(request.POST.get('menosDe70'))
        passageiro = {}
        ano_menos_70 = datetime.now().year - 35
        for _ in range(qtd_mais_70_anos):
            passageiro['nome'] = 'Desconhecido'
            passageiro['dataNascimento'] = f'{ano_menos_70}-01-01'
            passageiros.append(passageiro)

        data_saida = f'{request.POST.get("dataSaida")}'
        data_retorno = f'{request.POST.get("dataRetorno")}'

        cotacao_request = {
            "destinos": [
                destinos
            ],
            "passageiros": passageiros,
            "dataSaida": data_saida,
            "dataRetorno": data_retorno,
            "tipoViagem": 1,
            "tipoTarifa": 1,
            "produtoAvulso": False,
            "classificacoes": [
                1
            ]
        }
        print(cotacao_request)
        cotacao_response = requests.post(f'{base_url}/Cotacao', headers=headers, data=cotacao_request)
        print(cotacao_response.text)
        if cotacao_response != 200:
            return redirect('cotacao:erro')
        else:
            return redirect('cotacao:sucesso')
    
    return render(request, 'cotacao/home.html')
        