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
    email = forms.EmailInput()
    class Meta:
        model = Cliente
        fields = '__all__'
    
class FormEstacao(forms.ModelForm):
    senha_api = forms.CharField(widget=forms.PasswordInput(), required=False)
    status = forms.CharField(widget=forms.Select(
        choices=CHOICE_RADIO_STATUS
    ))
    data_expira = forms.DateField(widget=forms.DateInput(format="%d/%m/%Y"))
    def __init__(self, *args,**kwargs):
        super(FormEstacao, self).__init__(*args, **kwargs)

        self.fields['data_expira'].required = False
        self.fields['cliente'].label = 'Empresa'
        self.fields['data_expira'].widget.attrs.update({'data-toggle': "datepicker"})
    class Meta:
        model = Estacoes
        fields = '__all__'