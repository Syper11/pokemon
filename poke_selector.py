# import requests, json

# class pokemon():

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

# url = 'https://pokeapi.co/api/v2/pokemon/'

# pokequit = "yes"
# all_pokemon = []

# while pokequit != "no":
#   name = input("What is the name or number of the pokemon you are looking for? ")

#   my_pokemon = pokemon(name, (url+name))
#   if my_pokemon.getIsValid():
#     all_pokemon.append(my_pokemon)
#     print(my_pokemon)
#     print('\n')
#   else:
#       print('Not a pokemon entry try again!')
    
#   pokequit = input('\nDo you want to continue? "yes or no": ')

# print("\nHere is a list of your pokemon!\n")
# for poke in all_pokemon:
  
#   print(poke)


# print("Thanks for playing!!")