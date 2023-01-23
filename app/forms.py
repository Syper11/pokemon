from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PokemonSelect(FlaskForm):
    pokemon_name = StringField("Pokemon Name", validators = [DataRequired()])
    submit = SubmitField()
    print(pokemon_name)

# class Team(FlaskForm):
#     name = StringField("Pokemon Name", validators = [DataRequired()])
#     back_shiny = StringField("Back Shiny", validators = [DataRequired()])
#     ability = StringField("Ability", validators = [DataRequired()])
#     base_experience = StringField("Base Experience", validators = [DataRequired()])
#     attack_base = StringField("Base Attack", validators = [DataRequired()])
#     hp_base = StringField("Base HP", validators = [DataRequired()])
#     defense_base = StringField("Base Defense", validators = [DataRequired()])
#     submit = SubmitField()