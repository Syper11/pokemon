from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin

db = SQLAlchemy()


catchpokemon = db.Table(
    'catchpokemon',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), nullable=False),
    db.Column('pokemon_name', db.String, db.ForeignKey('searchpokemon.Pokemon_Name'), nullable=False)
)
   

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False, unique=True)
    last_name = db.Column(db.String(50), nullable=False, unique=True)
    username = db.Column(db.String(45), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    catch = db.relationship("SearchPokemon",
        secondary = catchpokemon,
        backref=db.backref('trainer', lazy='dynamic'),
        lazy = 'dynamic'
    )
    

    def __init__(self, first_name, last_name, username, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = password

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()

    def catching(self, pokemon):
        self.catch.append(pokemon)
        db.session.commit()

    def Releasing(self, user):
        self.catch.remove(user)
        db.session.commit()




class SearchPokemon(db.Model):
    __tablename__= 'searchpokemon'
    Search_id = db.Column(db.Integer, primary_key=True)
    Pokemon_Name = db.Column(db.String(200), nullable=False, unique=True)

    

    def __init__(self, Pokemon_Name):
        self.Pokemon_Name= Pokemon_Name
        

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()

