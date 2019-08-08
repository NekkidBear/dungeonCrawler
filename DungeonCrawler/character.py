import races
from random import randint


class BaseCharacter:
    stats = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]

    def __init__(self, x, y, name, race, xp, level, hp, archetype, strength, dexterity, constitution, intelligence,
                 wisdom, charisma,  skills=None):
        self.x = x
        self.y = y
        self.name = name
        self.race = race
        self.xp = xp
        self.level = level
        self.hp = hp
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.archetype = archetype
        self.skills = skills
        self.strength_modifier = 0
        self.dexterity_modifier = 0
        self.intelligence_modifier = 0
        self.wisdom_modifier = 0

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

    @classmethod
    def generate_player_character(cls):
        assigned = {}
        print("Every adventurer needs a name. How would you like to be known?")
        cls.name = input("Name: ")
        print("What race are you?")
        cls.race = input("Race: ")
        if cls.race not in races.races_constant:
            print("I'm not familiar with that race. Pick from " + str([r for r in races.races_constant]))
            print("Who are your people?")
            cls.race = input("Race: ")
        print("What kind of an adventurer are you--Rogue, Cleric, Wizard, Ranger, Paladin, Barbarian?")
        cls.archetype = input("Class: ")
        print("How would you like to determine your stats? a) roll for them, or b) standard array numbers?")
        stats_choice = input("A or B: ")
        if stats_choice in ['a', "A"]:
            print("Would you like me to roll the dice or would you like to? 1) computer rolls, 2)manual entry")
            rolls = input("Who rolls? ")
            if rolls in ["1", "computer" "computer rolls"]:
                print("One moment while I roll the dice and calculate your scores.")
                for s in cls.stats:
                    results = []
                    for d in range(4):
                        roll = randint(1, 6)
                        results.append(roll)
                    if len(results) == 4:
                        results.remove(min(results))
                    assigned[s] = sum(results)

            elif rolls in ["2", "manual", "manual entry"]:
                stats = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
                print("Roll 4 d6 and add the three highest rolls. Do this 6 times, and jot down the numbers.")
                for stat in stats:
                    print("What did you roll for %s " % stat)
                    val = int(input("? "))
                    assigned[stat] = val

        if stats_choice in ['b', "b"]:
            print("With the standard array, you get these scores to distribute as you see fit: ")
            print("15, 14, 13, 12, 10, 8")
            values = [15, 14, 13, 12, 10, 8]
            stats = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
            assigned = {}
            for s in stats:
                print("Which score would you like to assign to {}? ".format(s))
                value = input()
                assigned[s] = value
                values.remove(int(value))
                print("Remaining values: " + str(list(values)))
        # Calculate bonuses and saving throws

        return cls(0, 0, cls.name, cls.race, 0, 1, 0, cls.archetype,  **assigned)

    def __repr__(self):
        return f"""Character Stats
        Name:   {self.name.capitalize()}
        Race:   {self.race.capitalize()}
        Class:  {self.archetype.capitalize()}
        STR:    {self.strength}
        DEX:    {self.dexterity}
        CONST:  {self.constitution}
        INT:    {self.intelligence}
        WISD:   {self.wisdom}
        CHAR:   {self.charisma}
"""
