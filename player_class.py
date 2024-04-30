from random import randint
from typing import Type, Dict
import os

from choose_race import SelectRace

class Skill:
    def __init__(self, base_ability: str) -> None:
        self.base_ability: str = base_ability
        self.score = 0
        self.proficient: bool = False

    def AddProficiency(self) -> None:
        self.proficient = True

    def AddScore(self, number: int) -> None:
        self.score = number

class Character:
    def __init__(self, name: str):
        self.name: str = name
        self.level: int = 0
        self.hp: int = 0

        self.char_class: str = ""
        self.armor_class: int = 0

        self.ability_scores: Dict[str, int] = {
            "STR": 0,
            "DEX": 0,
            "CON": 0,
            "INT": 0,
            "WIS": 0,
            "CHA": 0
        }

        self.skill_tree: Dict[str, Type("Skill")] = {
                "Athletics": Skill("STR"),
                "Acrobatics": Skill("DEX"),
                "Slieght of Hand": Skill("DEX"),
                "Stealth": Skill("DEX"),
                "Arcana": Skill("INT"),
                "History": Skill("INT"),
                "Investigation": Skill("INT"),
                "Nature": Skill("INT"),
                "Religion": Skill("INT"),
                "Animal Handling": Skill("WIS"),
                "Insight": Skill("WIS"),
                "Medicine": Skill("WIS"),
                "Perception": Skill("WIS"),
                "Survival": Skill("WIS"),
                "Deception": Skill("CHA"),
                "Intimidation": Skill("CHA"),
                "Performance": Skill("CHA"),
                "Persuasion": Skill("CHA")
        }


        self.equipment: list = []

        #self.SelectAbilityScores()

        SelectRace(self)
        self.clear_screen()
        for _ in range(3):
            print(f"The Athletics roll is: {self.GetSkillCheck('Athletics')}")

    def SelectAbilityScores(self) -> None:
        score_rolls: list[int] = []

        for _ in range(6):
            random_rolls:list = [randint(1,6) for _ in range(4)]
            random_rolls.sort()
            score_rolls.append(sum(random_rolls[1::]))

        for key in self.ability_scores:

            user_input: int = 0

            while not isinstance(user_input, int) or user_input not in score_rolls:
                self.clear_screen()

                for roll in score_rolls:
                    print(roll)

                try:
                    user_input = int(input(f"Please input your {key} score from the list above: "))
                except ValueError:
                    print("Input not a number, please try again.")
                    input("Press <Enter> to continue...")
                    continue

                if user_input not in score_rolls:
                    print("Input not in list, please try again.")
                    input("Press <Enter> to continue...")


            self.ability_scores[key] = user_input

            score_rolls.remove(user_input)

        for key, value in self.ability_scores.items():
            print(f"{key}: {value}")

    def GetSkillCheck(self, skill_name: str) -> int:
        skill = self.skill_tree[skill_name]

        modifier: int = int((self.ability_scores[skill.base_ability] - 10) / 2)

        proficiency: int = 1 if skill.proficient else 0

        return randint(1, 20) + modifier + proficiency

    @staticmethod
    def clear_screen() -> None:
        os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    player = Character("pyko")
