# Generated by Django 4.0.2 on 2022-02-15 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_remove_pendencias_aprovado_recusado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cnpj',
            field=models.CharField(max_length=18, verbose_name='CNPJ'),
        ),
    ]
