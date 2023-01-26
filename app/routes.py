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
def friendly_battle():
    return render_template('friendly_battle.html')


@app.route('/poke_selection', methods=['GET','POST'])
@login_required
def Searching():
    form = PokemonSelect()
    url = 'https://pokeapi.co/api/v2/pokemon/'
    if request.method == 'POST':
        if form.validate():
            # binding
            pokemon_name = form.pokemon_name.data
            print(pokemon_name)
            specs = get_pokemon(url + pokemon_name)
            search = SearchPokemon.query.filter_by(Pokemon_Name =pokemon_name).first()
            if not search:
                search = SearchPokemon(pokemon_name)
                search.saveToDB()
            return render_template('poke_selection.html',form = form, specs = specs)

    return render_template('poke_selection.html',form = form)

@app.route('/catch/<pokemon_name>', methods=['GET','POST'])
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
    

@app.route('/user', methods=['GET','POST'])
@login_required
def userpage():
    form = PokemonSelect()
    url = 'https://pokeapi.co/api/v2/pokemon/'
    if request.method == 'GET':
        if form.validate():
            pokemon_name = form.User.query.all()
           
            print(pokemon_name)
            spec = get_pokemon(url + pokemon_name)
            return render_template('user.html', form=form, spec = spec)
    return render_template('user.html', form=form)

# @app.route('/user/release/', methods=['GET','POST'])
# @login_required
# def Release(pokemon_name):
#     pass
#     # pokeName = User.query.get(user_id=current_user, pokemon_name=pokemon_name).first()
#     # if pokeName:
#     #     pokeName.deleteFromDB()

#     # return render_template('poke_selection.html')