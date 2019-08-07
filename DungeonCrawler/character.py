import races
from random import randint


class BaseCharacter:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.name = None
        self.race = None
        self.xp = None
        self.level = None
        self.hp = 0
        self.strength = None
        self.dexterity = None
        self.constitution = None
        self.intelligence = None
        self.wisdom = None
        self.charisma = None
        self.archetype = None
        self.skills = []
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
    def __init__(self):
        pass

    def generate_character(self):
        print("Every adventurer needs a name. How would you like to be known?")
        self.name = input("Name: ")
        print("What race are you?")
        self.race = input("Race: ")
        if self.race not in races.races_constant:
            print("I'm not familiar with that race. Pick from " + str([r for r in races.races_constant]))
            print("Who are your people?")
            self.race = input("Race: ")
        print("What kind of an adventurer are you--Rogue, Cleric, Wizard, Ranger, Paladin, Barbarian?")
        self.archetype = input("Class: ")
        print("How would you like to determine your stats? a) roll for them, or b) standard array numbers?")
        stats_choice = input("A or B: ")
        if stats_choice in ['a', "A"]:
            print("Would you like me to roll the dice or would you like to? 1) computer rolls, 2)manual entry")
            rolls = input("Who rolls? ")
            if rolls in ["1", "computer" "computer rolls"]:
                print("One moment while I roll the dice and calculate your scores.")
                scores = []
                for i in range(6):
                    results = []
                    for d in range(4):
                        roll = randint(1, 6)
                        results.append(roll)
                    if len(results) == 4:
                        results.remove(min(results))
                    scores.append(sum(results))
                self.strength = scores[0]
                print("Strength: {}".format(self.strength))
                self.dexterity = scores[1]
                print("Dex: {}".format(self.dexterity))
                self.constitution = scores[2]
                print("Con: {}".format(self.constitution))
                self.intelligence = scores[3]
                print("INT: {}".format(self.intelligence))
                self.wisdom = scores[4]
                print("WIS: {}".format(self.wisdom))
                self.charisma = scores[5]
                print("Char: {}".format(self.charisma))
            elif rolls in ["2", "manual", "manual entry"]:
                print("Roll 4 d6 and add the three highest rolls. Do this 6 times, and jot down the numbers.")
                self.strength = input("What did you roll for strength? ")
                self.dexterity = input("What did you roll for dexterity? ")
                self.constitution = input("And for constitution? ")
                self.intelligence = input("Intelligence: ")
                self.wisdom = input("Wisdom: ")
                self.charisma = input("and Charisma: ")
        if stats_choice in ['b', "b"]:
            print("With the standard array, you get these scores to distribute as you see fit: ")
            print("15, 14, 13, 12, 10, 8")
            values = [15, 14, 13, 12, 10, 8]
            stats = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
            for s in stats:
                print("Which score would you like to assign to {}? ".format(s))
                values.remove(self.strength)
