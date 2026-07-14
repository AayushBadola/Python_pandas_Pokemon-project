import os


def clear_screen():
    """
    Clears the terminal screen.
    """

    os.system("cls" if os.name == "nt" else "clear")


def print_separator():
    """
    Prints a separator line.
    """

    print("=" * 50)


def print_title(title):
    """
    Prints a centered title.
    """

    print_separator()
    print(title.center(50))
    print_separator()


def pause():
    """
    Waits for the user before continuing.
    """

    input("\nPress Enter to continue...")


def print_main_menu():
    """
    Prints the main menu.
    """

    print("\n1. Show All Information")
    print("2. Show Selected Information")
    print("3. Battle Analysis")
    print("4. Fun Fact")
    print("5. Search Another Pokemon")
    print("6. Exit")


def print_selected_menu():
    """
    Prints the selected information menu.
    """

    print("\n1. Height")
    print("2. Weight")
    print("3. Types")
    print("4. Legendary")


def display_pokemon(pokemon):
    """
    Displays all information about a Pokemon.
    """

    print_title(pokemon["Name"])

    print(f"Number      : {pokemon['No']}")
    print(f"Type 1      : {pokemon['Type1']}")
    print(f"Type 2      : {pokemon['Type2']}")
    print(f"Height      : {pokemon['Height']} m")
    print(f"Weight      : {pokemon['Weight']} kg")

    legendary = "Yes" if pokemon["Legendary"] == 1 else "No"

    print(f"Legendary   : {legendary}")


def display_battle(result):
    """
    Displays battle recommendations.
    """

    print_title("Battle Analysis")

    print("Weaknesses")

    print(
        "Type 1:",
        ", ".join(result["Weakness Type1"])
    )

    if result["Weakness Type2"]:
        print(
            "Type 2:",
            ", ".join(result["Weakness Type2"])
        )

    print("\nRecommended Pokemon")

    if result["Recommended Pokemon"]:

        for pokemon in result["Recommended Pokemon"]:
            print(f"- {pokemon}")

    else:

        print("No recommended Pokemon found.")


def display_funfact(funfact):
    """
    Displays a Pokemon fun fact.
    """

    print_title("Fun Fact")
    print(funfact)