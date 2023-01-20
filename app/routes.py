from app import app
from flask import render_template


@app.route('/')
def homepage():
    people = ['Brett','Jordan']
    return render_template('index.html', people = people)

@app.route('/friendly_battle')
def friendly_battle():
    return render_template('friendly_battle.html')


@app.route('/poke_selection')
def apoke_selection():
    return render_template('poke_selection.html')
