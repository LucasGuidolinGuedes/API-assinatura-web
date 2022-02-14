
from django.urls import path
from .views import *


testeassinatura = TesteAssinatura()
view_cadastro = Cadastros()
view_tabelas = Tabelas()
view_updates = Updates()
view_deletes = Deletes()

urlpatterns = [
    path('', home),
    path('telaassinatura/', testeassinatura.telaassinatura, name='telaassinatura')
]

cadastros = [
    path('cadastro-grupo-empresa/', view_cadastro.cadastro_grupo_empresa, name='cadastro_grupo_empresa'),
]

tabelas = [
    path('tabela-grupo-empresa/', view_tabelas.tabela_grupo_empresa, name='tabela_grupo_empresa'),
]

updates = [
    path('update-grupo-empresa/<int:id>', view_updates.update_grupo_empresa, name='update_grupo_empresa'),
]

deletes = [
    path('delete-grupo-empresa/<int:id>', view_deletes.delete_grupo_empresa, name="delete_grupo_empresa")
]

for i in cadastros:
    urlpatterns.append(i)

for i in tabelas:
    urlpatterns.append(i)

for i in updates:
    urlpatterns.append(i)

for i in deletes:
    urlpatterns.append(i)