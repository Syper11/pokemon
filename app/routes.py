from app import app, auth
from flask import render_template, request, flash, url_for
from .forms import PokemonSelect
from pokemon import pokemon



@app.route('/')
def homepage():
    return render_template('index.html')

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

# @app.route('/poke_selection', methods = ["GET","POST"])
# def AddPokemon():
#     form = Team()
#     if request.method == "POST":
#         if form.validate():
#             name= form.name.data
#             back_shiny= form.back_shiny.data
#             ability= form.ability.data
#             base_experience= form.base_experience.data
#             attack_base= form.attack_base.data
#             hp_base= form.hp_base.data
#             defense_base= form.defense_base.data

#             post = Post(name, back_shiny, ability, base_experience, attack_base, hp_base, defense_base, auth.current_user.username)
#             post.saveToDB()


#     return render_template('poke_selection.html',form= form)

