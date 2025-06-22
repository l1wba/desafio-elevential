
from django.db import models

#------------------------------MODEL TIPO------------------------------

class Tipo(models.Model):
    nome = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nome

#------------------------------MODEL POKEMON/FOREIGN KEY------------------------------

class Pokemon(models.Model):
    nome = models.CharField(max_length=20)
    tipo_primario = models.ForeignKey(
        Tipo,
        on_delete=models.CASCADE,
        related_name='pokemons_primarios'
    )
    tipo_secundario = models.ForeignKey(
        Tipo,
        on_delete=models.SET_NULL,
        related_name='pokemons_secundarios',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.nome