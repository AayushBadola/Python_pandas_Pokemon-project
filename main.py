from pokedex import search_pokemon, did_you_mean
from battle import recommend_counter
from fun_fact import get_random_funfact

from utils import (
    clear_screen,
    pause,
    print_title,
    print_main_menu,
    print_selected_menu,
    display_pokemon,
    display_battle,
    display_funfact,
)


def main():

    clear_screen()
    print_title("WELCOME TO THE POKEDEX")

    while True:

        pokemon_name = input("\nEnter Pokemon Name (or EXIT): ").strip()

        if pokemon_name.upper() == "EXIT":
            clear_screen()
            print("Thank you for using the Pokedex!")
            break

        pokemon = search_pokemon(pokemon_name)

        # Pokemon not found
        if pokemon is None:

            suggestion = did_you_mean(pokemon_name)

            if suggestion:

                choice = input(
                    f"Did you mean {suggestion}? (Y/N): "
                ).strip().upper()

                if choice == "Y":
                    pokemon_name = suggestion
                    pokemon = search_pokemon(suggestion)

                else:
                    clear_screen()
                    continue

            else:
                print("Pokemon not found.")
                pause()
                clear_screen()
                continue

        # -------------------------
        # Pokemon Menu
        # -------------------------
        while True:

            clear_screen()
            print_title(pokemon["Name"])
            print_main_menu()

            option = input("\nEnter Choice: ").strip().upper()

            # Exit shortcut
            if option == "EXIT":
                clear_screen()
                print("Thank you for using the Pokedex!")
                return

            # -------------------------
            # Show All Information
            # -------------------------
            if option == "1":

                clear_screen()
                display_pokemon(pokemon)

                pause()

            # -------------------------
            # Show Selected Information
            # -------------------------
            elif option == "2":

                clear_screen()
                print_selected_menu()

                sub = input("\nChoice: ").strip()

                clear_screen()

                if sub == "1":

                    print_title("Height")
                    print(f"{pokemon['Height']} m")

                elif sub == "2":

                    print_title("Weight")
                    print(f"{pokemon['Weight']} kg")

                elif sub == "3":

                    print_title("Types")
                    print(f"Type 1 : {pokemon['Type1']}")
                    print(f"Type 2 : {pokemon['Type2']}")

                elif sub == "4":

                    print_title("Legendary Status")

                    if pokemon["Legendary"] == 1:
                        print("Yes")
                    else:
                        print("No")

                else:

                    print("Invalid Choice.")

                pause()

            # -------------------------
            # Battle Analysis
            # -------------------------
            elif option == "3":

                clear_screen()

                result = recommend_counter(pokemon_name)

                display_battle(result)

                pause()

            # -------------------------
            # Fun Fact
            # -------------------------
            elif option == "4":

                clear_screen()

                fact = get_random_funfact(pokemon_name)

                display_funfact(fact)

                pause()

            # -------------------------
            # Search Another Pokemon
            # -------------------------
            elif option == "5":

                clear_screen()
                break

            # -------------------------
            # Exit
            # -------------------------
            elif option == "6":

                clear_screen()
                print("Thank you for using the Pokedex!")
                return

            else:

                print("Invalid Choice.")
                pause()


if __name__ == "__main__":
    main()