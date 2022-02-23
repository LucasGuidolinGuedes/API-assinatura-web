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
import datetime
# Create your views here.

hoje = datetime.datetime.today()

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
   
        for i in grupos_empresa:
            if i.status == 0:
                status = 'Inativo'
            else:
                status = 'Ativo'

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

        try:
            colunas = list(datas[0].keys())
        except IndexError:
            colunas = []

        datas_values = md.formata_dicionario(datas)

        aprovar = False
        recusar = False
        excluir = True
        editar = True
        bt_novo = True

        titulo_card = 'Grupos de Empresas'
        descricao_botao_novo = 'Novo Grupo de Empresa'

        url_cadastro = '/cadastro-grupo-empresa/'
        url_update = '/update-grupo-empresa'
        url_delete = '/delete-grupo-empresa'

        return render(request, 'cruds/tabela/datatable.html', locals())

    def tabela_empresa(self, request):

        empresa = Cliente.objects.all()

        datas = []
    
        for i in empresa:
            if i.status == 0:
                status = 'Inativo'
            else:
                status = 'Ativo'

            dicionario = {
                'id': i.id,
                'Grupo Empresa': i.grupo_empresa.descricao,
                'CNPJ': f'{i.cnpj[0:2]}.{i.cnpj[2:5]}.{i.cnpj[5:8]}/{i.cnpj[8:12]}-{i.cnpj[12:14]}',
                'Razão Social': i.razao_social,
                'Nome Reduzido': i.nome_reduzido,
                'Telefone': f'({i.telefone[0:2]}) {i.telefone[2::]}',
                'email':i.email,
                'Status': status
            }

            datas.append(dicionario)
        try:
            colunas = list(datas[0].keys())
        except IndexError:
            colunas = []

        datas_values = md.formata_dicionario(datas)

        aprovar = False
        recusar = False
        excluir = True
        editar = True
        bt_novo = True

        titulo_card = 'Empresas'
        descricao_botao_novo = 'Nova Empresa'

        url_cadastro = '/cadastro-empresa/'
        url_update = '/update-empresa'
        url_delete = '/delete-empresa'

        return render(request, 'cruds/tabela/datatable.html', locals())

    def tabela_estacoes(self, request):

        empresa = Estacoes.objects.all()

        datas = []
        
        for i in empresa:
            if i.status == 0:
                status = 'Inativo'
            else:
                status = 'Ativo'
            
            if i.data_expira is None:
                expira_em = ''
            else:
                expira_em = formats.date_format(datetime.datetime.strptime(i.data_expira, '%d/%m/%Y').date(), "SHORT_DATE_FORMAT") 

            dicionario = {
                'id': i.id,
                'Serial da Maquina': i.serial_maquina,
                'Cliente': i.cliente.razao_social,
                'Expira em': expira_em,
                'Status': status
            }

            datas.append(dicionario)
        try:
            colunas = list(datas[0].keys())
        except IndexError:
            colunas = []

        datas_values = md.formata_dicionario(datas)

        aprovar = True
        recusar = True
        excluir = False
        editar = True
        bt_novo = False

        titulo_card = 'Estações'
        descricao_botao_novo = 'Nova Estação'

        url_cadastro = '#'
        url_update = '/update-estacao'
        url_delete = '#'
        url_aprovar = '/aprovar-estacao'
        url_recusar = '/recusar-estacao'

        return render(request, 'cruds/tabela/datatable.html', locals())

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
    
    def cadastro_empresa(self, request):
        
        titulo_card = 'Cadastrar Empresa'

        url_tabela = '/tabela-empresa/'

        if request.method == 'POST':
            forms = FormClientes(request.POST)
            cnpj = request.POST.get('cnpj')
            telefone = request.POST.get('telefone')
            if forms.is_valid():
                f = forms.save()
                f.cnpj = cnpj.replace('.', '').replace('/', '').replace('-', '')
                f.telefone = telefone.replace('(', '').replace(')', '').replace('-', '').replace(' ', '')
                f.save()
                return redirect('/tabela-empresa/')

        else:
            forms = FormClientes()

        return render(request, 'cruds/cadastros/cadastro-empresa.html', locals())

class Updates(View):
    def __init__(self, **kwargs):
        super(Updates).__init__(**kwargs)
    
    def update_grupo_empresa(self, request, id):

        
        try:
            obj_empresa = GrupoCliente.objects.get(id=id)
        except:
            print('erro em pegar o grupo de empresa')

        forms = FormGrupoClientes(request.POST or None, instance=obj_empresa)

        if forms.is_valid():
            forms.save()
            return redirect('/tabela-grupo-empresa/')

        return render(request, 'cruds/cadastros/cadastro-grupo-empresa.html', locals())

    def update_estacao(self, request, id):

        try:
            obj_estacao = Estacoes.objects.get(id=id)
        except:
            print('erro em pegar a estação')

        forms = FormEstacao(request.POST or None, instance=obj_estacao)

        if forms.is_valid():
            forms.save()
            return redirect('/tabela-estacoes/')

        return render(request, 'cruds/cadastros/cadastro-estacao.html', locals())

    def update_empresa(self, request, id):

        try:
            obj_empresa = Cliente.objects.get(id=id)
        except:
            print('erro em pegar a empresa')

        forms = FormClientes(request.POST or None, instance=obj_empresa)
        cnpj = request.POST.get('cnpj')
        telefone = request.POST.get('telefone')
        if forms.is_valid():
            f = forms.save()
            f.cnpj = cnpj.replace('.', '').replace('/', '').replace('-', '')
            f.telefone = telefone.replace('(', '').replace(')', '').replace('-', '').replace(' ', '')
            f.save()
            return redirect('/tabela-empresa/')

        return render(request, 'cruds/cadastros/cadastro-empresa.html', locals())
        
class Deletes(View):
    def __init__(self, **kwargs):
        super(Deletes).__init__(**kwargs)
    
    def delete_grupo_empresa(self, request, id):
        
        obj = GrupoCliente.objects.filter(id=id)

        obj.update(status=0)

        return redirect('/tabela-grupo-empresa/')

    def delete_empresa(self, request, id):
        
        obj = Cliente.objects.filter(id=id)

        obj.update(status=0)

        return redirect('/tabela-empresa/')

class Aprovar(View):
    def __init__(self, **kwargs):
        super(Aprovar).__init__(**kwargs)
    
    def aprovar_estacoes(self, request, id):

        obj = Estacoes.objects.filter(id=id)

        hoje_mais_30 = hoje + datetime.timedelta(days=30)

        hoje_mais_30_str = f'{hoje_mais_30.day}/{hoje_mais_30.month}/{hoje_mais_30.year}'

        obj.update(data_expira=hoje_mais_30_str)
        obj.update(status=1)

        return redirect('/tabela-estacoes/')

class Recusar(View):
    def __init__(self, **kwargs):
        super(Recusar).__init__(**kwargs)
    
    def recusar_estacoes(self, request, id):

        obj = Estacoes.objects.filter(id=id)

        obj.update(status=0)

        return redirect('/tabela-estacoes/')