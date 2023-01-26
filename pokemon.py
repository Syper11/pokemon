import requests, json

class pokemon():

    def __init__(self,name,pokedata):
        self.name = name
        self.specs = {}
        self.pokedata = pokedata
        self.__isValid = False
        # self.get_pokemon()
        

    def getIsValid(self):

        return self.__isValid    


    def get_pokemon(self):

        response = requests.get(self.pokedata)

        if response.ok:
            self.__isValid = True
            data = response.json()
            self.specs['name'] = data['name']
            self.specs["base_experience"] = data["base_experience"]
            self.specs["ability"] = data["abilities"][0]['ability']['name']
            self.specs["front_shiny"] = data["sprites"]["front_shiny"]
            self.specs["attack_base"] = data["stats"][1]["base_stat"]
            self.specs["hp_base"] = data["stats"][0]["base_stat"]
            self.specs["defense_base"] = data["stats"][2]["base_stat"]
            return self.specs
        
    def __repr__(self) -> str:
        
      return (f"Name:{self.specs['name']}\nBase EXP: {self.specs['base_experience']}\nAbility: {self.specs['ability']}\nShiny Images: {self.specs['front_shiny']}\n")