from pokemon import pokemon


class mainpoke():
    def __init__(self):
        self.url = 'https://pokeapi.co/api/v2/pokemon/'

    def Pokemon_main(self):
        
        pokequit = "yes"
        all_pokemon = []

        while pokequit != "no":
            name = input("What is the name or number of the pokemon you are looking for? ")

            my_pokemon = pokemon(name, (self.url+name))
            if my_pokemon.getIsValid():
                all_pokemon.append(my_pokemon)
                print(my_pokemon)
                print('\n')
            else:
                print('Not a pokemon entry try again!')
            
            pokequit = input('\nDo you want to continue? "yes or no": ')

        # print("\nHere is a list of your pokemon!\n")
        # for poke in all_pokemon:
        
        #     print(poke)
        return all_pokemon

    print("Thanks for playing!!")
