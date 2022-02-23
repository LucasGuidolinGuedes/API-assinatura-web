from rest_framework import serializers
from home import models

class Estacoes(serializers.ModelSerializer):
    class Meta:
        model = models.Estacoes
        fields = '__all__'

class Clientes(serializers.ModelSerializer):
    class Meta:
        model = models.Cliente
        fields = '__all__'