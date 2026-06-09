from django import forms
from .models import Objeto
from .models import RegistroPerda
from .models import RegistroEncontrado

class ObjetoForm(forms.ModelForm):

    class Meta:
        model = Objeto

        fields = [
            'nome',
            'descricao',
            'categoria',
            'tipo',
            'local',
            'status',
            'pessoa',   # <-- adicionar
        ]
class RegistroPerdaForm(forms.ModelForm):

    class Meta:
        model = RegistroPerda

        fields = [
            'pessoa',
            'objeto',
            'local',
            'descricao',
            
        ]


class RegistroEncontradoForm(forms.ModelForm):

    class Meta:
        model = RegistroEncontrado

        fields = [
            'objeto',
            'pessoa',
            'observacao'
        ]