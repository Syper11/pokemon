from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin

db = SQLAlchemy()

# create models from out ERD
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False, unique=True)
    last_name = db.Column(db.String(50), nullable=False, unique=True)
    username = db.Column(db.String(45), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    

    def __init__(self, first_name, last_name, username, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = password

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()


# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     back_shiny = db.Column(db.String(500), nullable=False, unique=True)
#     ability = db.Column(db.String(50), nullable=False, unique=True)
#     base_experience = db.Column(db.String(45), nullable=False, unique=True)
#     attack_base = db.Column(db.String(150), nullable=False, unique=True)
#     hp_base = db.Column(db.String, nullable=False)
#     defense_base = db.Column(db.String(50), nullable=False, unique=True)
#     username = db.Column(db.String, db.ForeignKey('User.username'), nullable=False)
    

#     def __init__(self, back_shiny, ability, base_experience, attack_base, hp_base, defense_base, username):
#         self.back_shiny = back_shiny
#         self.ability = ability
#         self.base_experience = base_experience
#         self.attack_base = attack_base
#         self.hp_base = hp_base
#         self.defense_base = defense_base
#         self.username = username

#     def saveToDB(self):
#         db.session.add(self)
#         db.session.commit()