from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    #------------------------------URLS LISTA POKEMONS/------------------------------

    path("lista/", views.lista, name="lista"),
    path("lista/criar-pokemon/", views.criar_pokemon, name= "criar_pokemon"),
    path("lista/editar-pokemon/<int:id>/", views.editar_pokemon, name="editar_pokemon"),
    path("lista/apagar-pokemon/<int:pokemon_id>/", views.apagar_pokemon, name="apagar_pokemon"),

    #------------------------------URLS LISTA TIPO/------------------------------
    
    path("lista-tipos/", views.lista_tipos, name= "lista-tipos"),
    path("lista-tipos/criar-tipo/", views.criar_tipo, name= "criar_tipo"),
    path("lista-tipos/editar-tipo/<int:id>/", views.editar_tipo, name="editar_tipo")
]