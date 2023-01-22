from app import app
from flask import render_template, request, flash
from .forms import PokemonSelect
from pokemon import pokemon


@app.route('/')
def homepage():
    people = ['Brett','Jordan']
    return render_template('index.html', people = people)

@app.route('/friendly_battle')
def friendly_battle():
    return render_template('friendly_battle.html')


@app.route('/poke_selection', methods=['GET','POST'])
def apoke_selection():
    form = PokemonSelect()
    url = 'https://pokeapi.co/api/v2/pokemon/'
    specs = {}
    if request.method == 'POST':
        if form.validate():
            # binding
            pokemon_name = form.pokemon_name.data
            print(pokemon_name)
            char = pokemon(pokemon_name, url + pokemon_name)
            specs = char.get_pokemon()
           

    return render_template('poke_selection.html',form = form, specs = specs)

