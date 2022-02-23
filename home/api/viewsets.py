from rest_framework import viewsets
from home.api import serializers
from home import models
from django_filters.rest_framework import DjangoFilterBackend

class EstacoesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.Estacoes
    queryset = models.Estacoes.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'cliente__cnpj', 'serial_maquina']

class ClienteViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.Clientes
    queryset = models.Cliente.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'cnpj']