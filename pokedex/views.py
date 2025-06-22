from django.shortcuts import render, redirect, get_object_or_404
from .models import Pokemon, Tipo
from .forms import TipoForm, PokemonForm

#------------------------------GET HOMEPAGE------------------------------

def home(request):
    return render(request, "home.html")

#------------------------------GET LISTAS------------------------------

def lista(request):
    pokemons = Pokemon.objects.all().order_by('id')
    return render(request, "lista.html", {'pokemons': pokemons})

def lista_tipos(request):
    tipos = Tipo.objects.all().order_by('id')
    return render(request, "lista-tipos.html", {'tipos': tipos})

#------------------------------GET CRIAR TIPOS/POKEMON------------------------------

def criar_pokemon(request):
    if request.method == "POST":
        form = PokemonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista") 
    else:
        form = PokemonForm()
    return render(request, 'criar-pokemon.html', {"form": form})

def criar_tipo(request):
    if request.method == "POST":
        form = TipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista-tipos')
    else:
        form = TipoForm()
    return render(request, "criar-tipo.html", {"form": form})

#------------------------------DELETE POKEMON/TIPO------------------------------

def apagar_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)
    pokemon.delete()
    return redirect("lista")

def apagar_tipo(request, tipo_id):
    pokemon = get_object_or_404(Tipo, id=tipo_id)
    pokemon.delete()
    return redirect("lista-tipos")

#------------------------------GET EDITAR POKEMON/TIPO------------------------------

def editar_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)

    if request.method == 'POST':
        form = PokemonForm(request.POST, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form = PokemonForm(instance=pokemon)

    return render(request, "editar-pokemon.html", {"form": form, "pokemon": pokemon})

def editar_tipo(request, tipo_id):
    tipo = get_object_or_404(Tipo, id=tipo_id)

    if request.method == 'POST':
        form = TipoForm(request.POST, instance=tipo)
        if form.is_valid():
            form.save()
            return redirect('lista-tipos')
    else:
        form = TipoForm(instance=tipo)
    return render (request, "editar-tipo.html", {"form": form, "tipo": tipo})
