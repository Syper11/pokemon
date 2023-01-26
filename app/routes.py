from app import app, auth
from flask import render_template, request, flash, url_for, redirect
from .forms import PokemonSelect
from .services import get_pokemon
from .models import SearchPokemon, User
from flask_login import current_user, login_required


@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/friendly_battle')
@login_required
def friendly_battle(user_id):
    form = SearchPokemon.query.find_by(user_id = user_id).all()

    return render_template('friendly_battle.html',form = form)


@app.route('/poke_selection', methods=['GET','POST'])
@login_required
def Searching():
    form = PokemonSelect()
    url = 'https://pokeapi.co/api/v2/pokemon/'
    if request.method == 'POST':
        if form.validate():
            # binding
            pokemon_name = form.pokemon_name.data
            
            specs = get_pokemon(url + pokemon_name)
            search = SearchPokemon.query.filter_by(Pokemon_Name =pokemon_name).first()
            if not search:
                search = SearchPokemon(pokemon_name)
                search.saveToDB()
            return render_template('poke_selection.html',form = form, specs = specs)

    return render_template('poke_selection.html',form = form)

@app.route('/catch/<string:pokemon_name>', methods=['GET','POST'])
@login_required
def Catch(pokemon_name):
    pokeName = SearchPokemon.query.filter_by(Pokemon_Name =pokemon_name).first()
    if pokeName:
        catch = current_user.catch.all()
        if len(catch) >= 5:
            print('No need to be greedy!')
        else:
            print('You cought a pokemon')
            current_user.catching(pokeName)

        return redirect(url_for('Searching'))
    
    return redirect(url_for('Searching'))
    

@app.route('/user', methods=['GET'])
@login_required
def userpage():
    pokename = current_user.catch
    if pokename:
        url = 'https://pokeapi.co/api/v2/pokemon/'
        pokemon= [p.Pokemon_Name for p in pokename]
        # poke = dict.fromkeys(pokemon, 1)
        poke = []
        print(poke)
        for name in pokemon:
            spec = get_pokemon(url + name)
            print(spec)
            poke.append(spec)
        return render_template('user.html', poke = poke)

   
@app.route('/user/<string:pokemon_name>', methods=['GET','POST'])
@login_required
def Release(pokemon_name):
    pokeName = SearchPokemon.query.filter_by(Pokemon_Name =pokemon_name).first()
    if pokeName:
        current_user.Releasing(pokeName)
        return redirect(url_for('Searching'))