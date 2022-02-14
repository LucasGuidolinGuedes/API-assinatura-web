from django import forms
from .models import *

CHOICE_RADIO_STATUS = [
    (1, 'Ativo'),
    (0, 'Inativo')
]

class FormGrupoClientes(forms.ModelForm):

    status = forms.CharField(widget=forms.Select(
        choices=CHOICE_RADIO_STATUS
    ))

    class Meta:
        model = GrupoCliente
        fields = '__all__'
    
class FormClientes(forms.ModelForm):

    status = forms.CharField(widget=forms.Select(
        choices=CHOICE_RADIO_STATUS
    ))

    class Meta:
        model = Cliente
        fields = '__all__'
    
class FormPendencias(forms.ModelForm):

    status = forms.CharField(widget=forms.Select(
        choices=CHOICE_RADIO_STATUS
    ))

    class Meta:
        model = Pendencias
        fields = '__all__'