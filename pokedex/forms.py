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

    def clean(self):
        cleaned_data = super().clean()
        tipo_primario = cleaned_data.get('tipo_primario')
        tipo_secundario = cleaned_data.get('tipo_secundario')

        if tipo_primario and tipo_secundario and tipo_primario == tipo_secundario:
            raise forms.ValidationError("O Tipo Primário e o Tipo Secundário não podem ser iguais.")

class TipoForm(forms.ModelForm):
    class Meta:
        model = Tipo
        fields = ['nome']
        labels = {
            'nome': 'Nome do Tipo',
        }