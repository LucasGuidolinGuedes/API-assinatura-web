# Generated by Django 4.0.2 on 2022-02-11 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GrupoCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=64, verbose_name='Descrição')),
                ('nomecontato', models.CharField(max_length=64, verbose_name='Nome do Contato')),
                ('telefone', models.CharField(max_length=25, verbose_name='Telefon')),
                ('email', models.CharField(max_length=128, verbose_name='Email')),
                ('apiuser', models.CharField(max_length=256, verbose_name='Username API')),
                ('apipass', models.CharField(max_length=256, verbose_name='Password API')),
                ('apitoken', models.CharField(max_length=256, verbose_name='Token API')),
                ('dtcadastro', models.DateTimeField(auto_now=True, verbose_name='Data do Cadastro')),
                ('status', models.IntegerField(verbose_name='Ativo')),
            ],
        ),
    ]
