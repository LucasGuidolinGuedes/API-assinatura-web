
from django.urls import path
from .views import *


testeassinatura = TesteAssinatura()

urlpatterns = [
    path('', home),
    path('datatable/', table, name='table'),
    path('telaassinatura/', testeassinatura.telaassinatura, name='telaassinatura')
]
