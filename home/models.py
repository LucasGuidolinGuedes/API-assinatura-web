import email
from django.db import models

class GrupoCliente(models.Model):
    descricao = models.CharField(u'Descrição', max_length=64)
    nomecontato = models.CharField(u'Nome do Contato', max_length=64)
    telefone = models.CharField(u'Telefone', max_length=25)
    email = models.CharField(u'Email', max_length=128)
    dtcadastro = models.DateTimeField(u'Data do Cadastro', auto_now=True)
    status = models.IntegerField(u'Ativo')

    def __str__(self) :
        return self.descricao

class Cliente(models.Model):
    grupo_emrpesa = models.ForeignKey("home.GrupoCliente", verbose_name="grupo_cliente_cliente", on_delete=models.CASCADE)
    cnpj = models.CharField(u"CNPJ", max_length=14)
    razao_social = models.CharField(u"Razão Social", max_length=64)
    nome_reduzido = models.CharField(u"Nome Reduzido", max_length=15)
    telefone = models.CharField(u"Telefone", max_length=25)
    email = models.CharField(u"Email", max_length=128)
    status = models.IntegerField(u'Ativo')

    def __str__(self):
        return self.razao_social
class Pendencias(models.Model):
    serial_maquina = models.CharField(u'Serial da Maquina', max_length=246)
    cliente = models.ForeignKey("home.Cliente", verbose_name="cliente_pendencias", on_delete=models.CASCADE)
    status = models.IntegerField(u'Ativo')

    def __str__(self):
        return self.serial_maquina