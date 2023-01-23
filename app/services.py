import requests, json

def get_pokemon(pokedata):

        response = requests.get(pokedata)
        spec = {}

        if response.ok:
            data = response.json()
            spec['name'] = data['name']
            spec["base_experience"] = data["base_experience"]
            spec["ability"] = data["abilities"][0]['ability']['name']
            spec["back_shiny"] = data["sprites"]["back_shiny"]
            spec["attack_base"] = data["stats"][1]["base_stat"]
            spec["hp_base"] = data["stats"][0]["base_stat"]
            spec["defense_base"] = data["stats"][2]["base_stat"]
            return spec
        else:
            return None