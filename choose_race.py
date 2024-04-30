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

    if user_input == "Dragonborn":
        character.ability_scores["STR"] += 2
        character.ability_scores["CHA"] += 1

    elif user_input == "Dwarf":
        character.ability_scores["CON"] += 2


    elif user_input == "Elf":
        character.ability_scores["DEX"] += 2

    elif user_input == "Gnome":
        character.ability_scores["INT"] += 2

    elif user_input == "Half-Elf":
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

    elif user_input == "Halfling":
        character.ability_scores["DEX"] += 2

    elif user_input == "Half-Orc":
        character.ability_scores["STR"] += 2
        character.ability_scores["CON"] += 1

    elif user_input == "Human":
        for key in character.ability_scores.keys():
            character.ability_scores[key] += 1

    elif user_input == "Tiefling":
        character.ability_scores["CHA"] += 2
        character.ability_scores["INT"] += 1
