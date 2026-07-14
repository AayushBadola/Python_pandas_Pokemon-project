from pokedex import search_pokemon
from data.type_chart import type_chart
from data_loader import load_data

# Load the cleaned dataset once
pokemon_df = load_data()


def get_weaknesses(pokemon_user):
    """
    Returns the weaknesses of a Pokemon based on its Type1 and Type2.

    Returns:
        weakness1 : list
        weakness2 : list (empty if no Type2)
    """

    pokemon = search_pokemon(pokemon_user)

    if pokemon is None:
        return None, None

    type1 = pokemon["Type1"]
    type2 = pokemon["Type2"]

    weakness1 = type_chart[type1]["weak_against"]

    if type2 != "None":
        weakness2 = type_chart[type2]["weak_against"]
    else:
        weakness2 = []

    return weakness1, weakness2


def generate_type_combinations(weakness1, weakness2):
    """
    Generates every possible type combination that is effective
    against the Pokemon.
    """

    combinations = set()

    # Pokemon has only one type
    if len(weakness2) == 0:

        for weakness in weakness1:
            combinations.add((weakness,))

        return list(combinations)

    # Pokemon has two types
    for type1 in weakness1:

        for type2 in weakness2:

            if type1 != type2:
                combinations.add((type1, type2))

    return list(combinations)


def recommend_counter(pokemon_user):
    """
    Returns Pokemon having the best type combinations to counter
    the given Pokemon.
    """

    pokemon = search_pokemon(pokemon_user)

    if pokemon is None:
        return None

    weakness1, weakness2 = get_weaknesses(pokemon_user)

    combinations = generate_type_combinations(
        weakness1,
        weakness2
    )

    recommended = set()

    for combination in combinations:

        # -----------------------------
        # Dual Type Search
        # -----------------------------
        if len(combination) == 2:

            type1, type2 = combination

            matches = pokemon_df[
                (
                    (pokemon_df["Type1"] == type1) &
                    (pokemon_df["Type2"] == type2)
                )
                |
                (
                    (pokemon_df["Type1"] == type2) &
                    (pokemon_df["Type2"] == type1)
                )
            ]

        # -----------------------------
        # Single Type Search
        # -----------------------------
        else:

            type1 = combination[0]

            matches = pokemon_df[
                (pokemon_df["Type1"] == type1)
                |
                (pokemon_df["Type2"] == type1)
            ]

        recommended.update(matches["Name"])

    return {
        "Weakness Type1": weakness1,
        "Weakness Type2": weakness2,
        "Recommended Pokemon": sorted(recommended)
    }
