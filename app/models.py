from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import requests, json

db = SQLAlchemy()

# create models from out ERD
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()

# class pokemon(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     img_url = db.Column(db.String, nullable=False)
#     caption = db.Column(db.String(1000))
#     date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

#     def __init__(self,name,pokedata):
#         self.name = name
#         self.specs = {}
#         self.pokedata = pokedata
#         self.__isValid = False
#         self.get_pokemon()

#     def getIsValid(self):

#         return self.__isValid 
#     def get_pokemon(self):

#         response = requests.get(self.pokedata)

#         if response.ok:
#             self.__isValid = True
#             data = response.json()
#             self.specs['name'] = data['name']
#             self.specs["base_experience"] = data["base_experience"]
#             self.specs["ability"] = data["abilities"][0]['ability']['name']
#             self.specs["back_shiny"] = data["sprites"]["back_shiny"]

    