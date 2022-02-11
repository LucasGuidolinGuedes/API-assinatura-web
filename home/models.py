import email
from django.db import models


class GrupoCliente(models.Model):
    descricao = models.CharField(u'Descrição', max_length=64)
    nomecontato = models.CharField(u'Nome do Contato', max_length=64)
    telefone = models.CharField(u'Telefon', max_length=25)
    email = models.CharField(u'Email', max_length=128)
    apiuser = models.CharField(u'Username API', max_length=256)
    apipass = models.CharField(u'Password API', max_length=256)
    apitoken = models.CharField(u'Token API', max_length=256)
    dtcadastro = models.DateTimeField(u'Data do Cadastro', auto_now=True)
    status = models.IntegerField(u'Ativo')

    def __str__(self) :
        return self.descricao