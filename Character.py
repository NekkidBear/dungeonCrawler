import Races
from random import randint


class BaseCharacter:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.name = None
        self.race = None
        self.xp = None
        self.level = None
        self.hp = None
        self.strength = None
        self.dexterity = None
        self.constitution = None
        self.intelligence = None
        self.wisdom = None
        self.charisma = None
        self.archetype = None
        self.skills = None
        self.strength_saving_throw = None
        self. dexterity_saving_throw = None
        self.constitution_saving_throw = None
        self.intelligence_saving_throw = None
        self.wisdom_saving_throw = None
        self.charisma_saving_throw = None
        self.temporary_hp = None
        self.heal_rate = None
        self.passive_perception = None
        self.death_save_success = None
        self.inventory = None
        self.gold = None
        self.max_spells_per_day_level_1 = None
        self.spell_slots_used_level_1 = None
        self.max_spells_per_day_level_2 = None
        self.spell_slots_used_level_2 = None
        self.max_spells_per_day_level_3 = None
        self.spell_slots_used_level_3 = None
        self.max_spells_per_day_level_4 = None
        self.spell_slots_used_level_4 = None
        self.max_spells_per_day_level_5 = None
        self.spell_slots_used_level_5 = None
        self.max_spells_per_day_level_6 = None
        self.spell_slots_used_level_6 = None
        self.max_spells_per_day_level_7 = None
        self.spell_slots_used_level_7 = None
        self.max_spells_per_day_level_8 = None
        self.spell_slots_used_level_8 = None
        self.max_spells_per_day_level_9 = None
        self.spell_slots_used_level_9 = None
        self.cantrips = None
        self.languages_spoken = None


class PlayerCharacter(BaseCharacter):
    def __init__(self, x, y):
        BaseCharacter.__init__(self, x, y)

    def generate_character(self):
        print("Every adventurer needs a name. How would you like to be known?")
        self.name = input("Name: ")
        print("What race are you?")
        self.race = input("Race: ")
        if self.race not in Races.races_constant:
            print("I'm not familiar with that race. Pick from " + str([r for r in Races.races_constant]))
        print("What kind of adventurer are you?")
        self.archetype = input("Class: ")
        print("How would you like to determine your stats? a) roll for them, or b)18-point buy in?")
        stats_choice = input("A or B")
        if stats_choice in ['a', "A"]:
            print("Would you like me to roll the dice or would you like to? 1) computer rolls, 2)manual entry")
            rolls = input("Who rolls?")
            if rolls in ["1", "computer" "computer rolls"]:
                print("One moment while I roll the dice and calculate your scores.")
                for i in range(6):
                    scores = []
                    for d in range(4):
                        results = []
                        roll = randint(1, 6)
                        results.append(roll)
                    results.remove(min(results))
                    scores.append(sum(results))
                self.strength = scores[0]
                self.dexterity = scores[1]
                self.constitution = scores[2]
                self.intelligence = scores[3]
                self.wisdom = scores[4]
                self.charisma = scores[5]
            elif rolls in["2", "manual", "manual entry"]:
                print("Roll 4 d6 and add the three highest rolls. Do this 6 times, and jot down the numbers.")
                self.strength = input("What did you roll for strength? ")
                self.dexterity = input("What did you roll for dexterity? ")
                self.constitution = input("And for constitution? ")
                self.intelligence = input("Intelligence: ")
                self.wisdom = input("Wisdom: ")
                self.charisma = input("and Charisma: ")
