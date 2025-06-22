from django import forms
from .models import Pokemon, Tipo

#------------------------------FORMS POST------------------------------

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = ['nome', 'tipo_primario', 'tipo_secundario']
        labels = {
            'nome': 'Nome do Pokémon',
            'tipo_primario': 'Tipo Primário',
            'tipo_secundario': 'Tipo Secundário',
        }

class TipoForm(forms.ModelForm):
    class Meta:
        model = Tipo
        fields = ['nome']
        labels = {
            'nome': 'Nome do Tipo',
        }