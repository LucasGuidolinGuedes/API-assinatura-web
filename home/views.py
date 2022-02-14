from datetime import date
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.views import View
import requests
import base64
import json
from django.templatetags.static import static
import os
from .modulos import modulos as md
from .forms import *
from .models import *
from django.utils import formats
# Create your views here.

def home(request):
    
    return render(request, 'base.html', locals())
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

class Tabelas(View):
    def __init__(self):
        super(Tabelas).__init__()

    def tabela_grupo_empresa(self, request):

        grupos_empresa = GrupoCliente.objects.all()

        datas = []
        status = 'Ativo'
        for i in grupos_empresa:
            if i.status == 0:
                status = 'Inativo'

            dicionario = {
                'id': i.id,
                'Descrição': i.descricao,
                'Nome do Contato': i.nomecontato,
                'Telefone': i.telefone,
                'email': i.email,
                'Data de Cadastro': formats.date_format(i.dtcadastro, "SHORT_DATETIME_FORMAT"),
                'Status': status
            }

            datas.append(dicionario)

        colunas = list(datas[0].keys())

        datas_values = md.formata_dicionario(datas)

        aprovar = False
        recusar = False
        excluir = True
        editar = True

        titulo_card = 'Grupos de Empresas'
        descricao_botao_novo = 'Novo Grupo de Empresa'

        url_cadastro = '/cadastro-grupo-empresa/'
        url_update = '/update-grupo-empresa'
        url_delete = '/delete-grupo-empresa'

        return render(request, 'cruds/tabelas/datatable.html', locals())

class Cadastros(View):
    def __init__(self, **kwargs):
        super(Cadastros).__init__(**kwargs)


    def cadastro_grupo_empresa(self, request):
        
        titulo_card = 'Cadastrar Grupo de Empresa'

        url_tabela = '/tabela-grupo-empresa/'

        if request.method == 'POST':
            forms = FormGrupoClientes(request.POST)
         
            if forms.is_valid():
                f = forms.save()
                return redirect('/tabela-grupo-empresa/')

        else:
            forms = FormGrupoClientes()

        return render(request, 'cruds/cadastros/cadastro-grupo-empresa.html', locals())


class Updates(View):
    def __init__(self, **kwargs):
        super(Updates).__init__(**kwargs)
    
    def update_grupo_empresa(self, request, id):
        
        try:
            obj_empresa = GrupoCliente.objects.get(id=id)
        except:
            print('erro em pegar a empresa')
        forms = FormGrupoClientes(request.POST or None, instance=obj_empresa)

        if forms.is_valid():
            forms.save()
            return redirect('/tabela-grupo-empresa/')

        return render(request, 'cruds/cadastros/cadastro-grupo-empresa.html', locals())


class Deletes(View):
    def __init__(self, **kwargs):
        super(Deletes).__init__(**kwargs)
    
    def delete_grupo_empresa(self, request, id):
        
        obj = GrupoCliente.objects.filter(id=id)

        obj.update(status=0)

        return redirect('/tabela-grupo-empresa/')