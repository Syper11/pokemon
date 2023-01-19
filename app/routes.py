from app import app
from flask import render_template, request, redirect, url_for
from .forms import UserCreationForm
from .models import User

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


@app.route('/signup', methods=["GET", "POST"])
def signUpPage():
    form = UserCreationForm()
    print(request.method)
    if request.method == 'POST':
        if form.validate():
            username = form.username.data
            email = form.email.data
            password = form.password.data
            
            print(username, email, password)

            # add user to database
            user = User(username, email, password)
            print(user)

            user.saveToDB()

            return redirect(url_for('friendly_battle'))


    return render_template('signup.html', form = form )

@app.route('/login')
def login():
    return render_template('login.html')