import random 
from data.fun_fact_data import pokemon_facts

# we plug in the value the user enters and based on that if user selects a pokemon and need fun-fact about it we will generate a random funfact 
unused_facts = {} # to store facts which have not been used 
def get_random_funfact(pokemon):
    """
    Returns a random unused fun fact for the given Pokémon.
    Once all facts have been shown, the facts are reshuffled and reused.
    """   
    pokemon = pokemon.upper() # defensive programming altough change string by user to upper when we take input we still change it to upper 
    # we change it to upper for the sake of consistence other wise if user provides PikaChu then we will have trouble in selecting the "Key"

    # if pokemon is not there (this is again a edfensive programming since while taking input from user we ll take care of it )
    if pokemon not in pokemon_facts:

        return "Pokemon Not Found"

    # first time calling the facts or all facts have been emptied 
    if pokemon not in unused_facts or len(unused_facts[pokemon] ) == 0:
        unused_facts[pokemon]  = pokemon_facts[pokemon].copy()

        # shuffel the facts also so the 2nd call wil not result in the result we got in 1st call
        random.shuffle(unused_facts[pokemon])

    return unused_facts[pokemon].pop()

# this logic is basically for any pokemon Pikachu when we want a fun fact it it will generate it at random from 5 given funfact 
# when that is done and we want funfact again for pikachu we use the remaining 4 facts which were not used and then randomly select one 
# it will happen till we reach 0 and we start over for that pokemon 



