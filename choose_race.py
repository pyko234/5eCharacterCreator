from random import randint
from typing import Type, Dict

def SelectRace(character: Type["Character"]) -> None:
    races: list[str] = [
        "Dragonborn",
        "Dwarf",
        "Elf",
        "Gnome",
        "Half-Elf",
        "Halfling",
        "Half-Orc",
        "Human",
        "Tiefling"
    ]

    user_input = ''

    character.clear_screen()
    while user_input not in races:
        print(', '.join(map(str, races)))
        user_input = input("Please enter a race from the list above: ")

        if user_input not in races:
            print("Selected race not in list, please try again")
            input("Press enter to continue...")
            character.clear_screen()

    match user_input:
        case "Dragonborn":
            character.ability_scores["STR"] += 2
            character.ability_scores["CHA"] += 1

        case "Dwarf":
            character.ability_scores["CON"] += 2


        case "Elf":
            character.ability_scores["DEX"] += 2

        case "Gnome":
            character.ability_scores["INT"] += 2

        case "Half-Elf":
            character.ability_scores["CHA"] += 2
            character.clear_screen()
            while user_input not in character.ability_scores.keys():
                print(', '.join(map(str, character.ability_scores.keys())))
                user_input = input("Please select an ability score to increase from the list above: ")
                if user_input not in character.ability_scores.keys():
                    print("Selection not in list.")
                    input("Press enter to continue...")
                    character.clear_screen()

            character.ability_scores[user_input] += 1

        case "Halfling":
            character.ability_scores["DEX"] += 2

        case "Half-Orc":
            character.ability_scores["STR"] += 2
            character.ability_scores["CON"] += 1

        case "Human":
            for key in character.ability_scores.keys():
                character.ability_scores[key] += 1

        case "Tiefling":
            character.ability_scores["CHA"] += 2
            character.ability_scores["INT"] += 1
