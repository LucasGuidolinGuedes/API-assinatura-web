from django.shortcuts import render
from django.views import View
import requests
import base64
import json
from django.templatetags.static import static
import os
from .modulos import modulos as md

# Create your views here.

def home(request):
    
    return render(request, 'base.html', locals())


def table(request):

    titulo_card = 'Tabela de teste'
    


    datas = [{
            'coluna1': 'um',
            'coluna2': 'dois',
            'coluna3': 'tres',
            'coluna4': 'quatro'
        },
        {
            'coluna1': 'um',
            'coluna2': 'dois',
            'coluna3': 'tres',
            'coluna4': 'quatro'
        },
        {
            'coluna1': 'um',
            'coluna2': 'dois',
            'coluna3': 'tres',
            'coluna4': 'quatro'
        },
        {
            'coluna1': 'um',
            'coluna2': 'dois',
            'coluna3': 'tres',
            'coluna4': 'quatro'
        },
    ]

    colunas = list(datas[0].keys())

    datas_values = md.formata_dicionario(datas)
    
    aprovar = True
    recusar = True
    excluir = True

    return render(request, 'cruds/tabelas/datatable.html', locals())


class TesteAssinatura(View):
    def __init__(self, **kwargs):
        super(TesteAssinatura).__init__(**kwargs)

    def telaassinatura(self, request):
        titulo_card = 'Teste de assinatura'

        if request.method == 'POST':
            try:
                get_assinatura =  requests.get('http://192.168.1.22:5689/abrirtela')
                
                imagem_64 = json.loads(get_assinatura.content)
            
                cwd = os.getcwd()   
                fileassi = cwd + '\\home\\static\\assinatura.png'
            
                with open(fileassi, "wb") as fh:
                    fh.write(base64.b64decode(imagem_64['img64']))

            except Exception as e:
                print('erro por não conseguir chamar a api')

        return render(request, 'testarassinatura/tela.html', locals())