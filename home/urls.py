
from unicodedata import name
from django.urls import path, include
from .views import *
from rest_framework import routers
from home.api import viewsets

route = routers.DefaultRouter()

route.register(r'api-estacoes', viewsets.EstacoesViewSet, basename='api_estacoes')
route.register(r'api-clientes', viewsets.ClienteViewSet, basename='api_clientes')

testeassinatura = TesteAssinatura()
view_cadastro = Cadastros()
view_tabelas = Tabelas()
view_updates = Updates()
view_deletes = Deletes()
view_aprovar = Aprovar()
view_recusar = Recusar()

urlpatterns = [
    path('', home),
    path('', include(route.urls)),
    path('telaassinatura/', testeassinatura.telaassinatura, name='telaassinatura')
]

tabelas = [
    path('tabela-grupo-empresa/', view_tabelas.tabela_grupo_empresa, name='tabela_grupo_empresa'),
    path('tabela-empresa/', view_tabelas.tabela_empresa, name='tabela_empresa'),
    path('tabela-estacoes/', view_tabelas.tabela_estacoes, name='tabela_pendencias')
]

cadastros = [
    path('cadastro-grupo-empresa/', view_cadastro.cadastro_grupo_empresa, name='cadastro_grupo_empresa'),
    path('cadastro-empresa/', view_cadastro.cadastro_empresa, name='cadastro_empresa'),
]

updates = [
    path('update-grupo-empresa/<int:id>', view_updates.update_grupo_empresa, name='update_grupo_empresa'),
    path('update-empresa/<int:id>', view_updates.update_empresa, name='update_empresa'),
    path('update-estacao/<int:id>', view_updates.update_estacao, name='update_estacao'),
]

deletes = [
    path('delete-grupo-empresa/<int:id>', view_deletes.delete_grupo_empresa, name="delete_grupo_empresa"),
    path('delete-empresa/<int:id>', view_deletes.delete_empresa, name="delete_empresa")
]

aceitos = [
    path('aprovar-estacao/<int:id>', view_aprovar.aprovar_estacoes, name='aprovar_pendencia')
]

recusados = [
    path('recusar-estacao/<int:id>', view_recusar.recusar_estacoes, name='recusar_pendencia')
]

for i in cadastros:
    urlpatterns.append(i)

for i in tabelas:
    urlpatterns.append(i)

for i in updates:
    urlpatterns.append(i)

for i in deletes:
    urlpatterns.append(i)

for i in aceitos:
    urlpatterns.append(i)

for i in recusados:
    urlpatterns.append(i)