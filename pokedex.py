from data_loader import load_data # to work with the workable data 
import difflib 

# loading the merged data we built after cleaning 2 datasets in clean_data which basically gives us the clean data and then

# we get merged data fomr load_data
pokemon_df = load_data()
# Checking if the said pokmeon exist in gen 1 or gen 2 (RETURNS TRUE OR FALSE)
def pokemon_exist(pokemon):
    pokemon_name = pokemon.strip().title()

    return pokemon_name in pokemon_df["Name"].values



def search_pokemon(pokemon_name):
    """
    Searches the Pokedex for a Pokemon.

    Returns:
        Pandas Series containing the Pokemon information.
        Returns None if the Pokemon does not exist.
    """

    # Defensive programming
    pokemon_name = pokemon_name.strip().upper()

    # Compare uppercase to uppercase
    pokemon = pokemon_df[
        pokemon_df["Name"].str.upper() == pokemon_name
    ]

    if pokemon.empty:
        return None

    return pokemon.iloc[0]



def did_you_mean(pokemon_name):
    """
    Suggests the closest Pokemon name if the user misspells it.

    Returns:
        Pokemon name if found.
        None otherwise.
    """

    pokemon_name = pokemon_name.strip()

    matches = difflib.get_close_matches(
        pokemon_name,
        pokemon_df["Name"],
        n=1,
        cutoff=0.6
    )

    if matches:
        return matches[0]

    return None