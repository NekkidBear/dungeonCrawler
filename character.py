from races import *
from archetypes import *
from random import randint


class BaseCharacter:
    stats = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
    races_dict = {"dragon-born": DragonBorn(), "dwarf": Dwarf(), "elf": Elf(), "gnome": Gnome(), "half-elf": HalfElf(),
                  "halfling": Halfling(), "half-orc": HalfOrc(), "human": Human(), "tiefling": Tiefling()}
    archetype_dict = {"cleric": Cleric(), "rogue": Rogue(), "barbarian": Barbarian(), "wizard": Wizard(),
                      "paladin": Paladin(), "ranger": Ranger()}

    def __init__(self, x, y, name, race, xp, archetype, strength, dexterity, constitution, intelligence,
                 wisdom, charisma):
        self.x = x
        self.y = y
        self.name = name
        self.race = race
        self.xp = xp
        self.multi_class = {archetype.name: archetype.career_level}
        self.level = sum(self.multi_class.values())
        self.base_strength = strength
        self.base_dexterity = dexterity
        self.base_constitution = constitution
        self.base_intelligence = intelligence
        self.base_wisdom = wisdom
        self.base_charisma = charisma
        self.strength = self.base_strength + self.races_dict[race.lower()].racial_str_bonus
        self.dexterity = self.base_dexterity + self.races_dict[race.lower()].racial_dex_bonus
        self.constitution = self.base_constitution + self.races_dict[race.lower()].racial_const_bonus
        self.intelligence = self.base_intelligence + self.races_dict[race.lower()].racial_int_bonus
        self.wisdom = self.base_wisdom + self.races_dict[race.lower()].racial_wis_bonus
        self.charisma = self.base_charisma + self.races_dict[race.lower()].racial_char_bonus
        self.stat_block = {"strength": strength, "dexterity": dexterity, "constitution": constitution,
                           "intelligence": intelligence, "wisdom": wisdom, "charisma": charisma}

        self.strength_modifier = self.determine_modifiers(self.strength)
        self.constitution_modifier = self.determine_modifiers(self.constitution)
        self.dexterity_modifier = self.determine_modifiers(self.dexterity)
        self.intelligence_modifier = self.determine_modifiers(self.intelligence)
        self.wisdom_modifier = self.determine_modifiers(self.wisdom)
        self.charisma_modifier = self.determine_modifiers(self.charisma)

        self.archetype = archetype.name
        self.skills = archetype.skills

        self.strength_saving_throw = None
        self. dexterity_saving_throw = None
        self.constitution_saving_throw = None
        self.intelligence_saving_throw = None
        self.wisdom_saving_throw = None
        self.charisma_saving_throw = None

        self.temporary_hp = None
        self.passive_perception = None
        self.death_save_success = None
        self.inventory = None
        self.gold = None
        self.languages_spoken = None

    @classmethod
    def generate_character(cls):
        assigned = {}
        # Get player character's name
        print("Every adventurer needs a name. How would you like to be known?")
        cls.name = input("Name: ")

        # get character's race
        print("What race are you?")
        for key in cls.races_dict:
            print(key)
        cls.race = input("Race: ")
        while cls.race.lower() not in cls.races_dict:
            print("I'm not familiar with that race. Pick from:")
            for key in cls.races_dict:
                print(key)
            print("Who are your people?")
            cls.race = input("Race: ")
        cls.races_dict[cls.race].build()

        # get class (variable is named archetype because 'class' is a reserved word in Python)
        print("What kind of an adventurer are you--Rogue, Cleric, Wizard, Ranger, Paladin, Barbarian?")
        cls.archetype = input("Class: ")
        cls.archetype_dict[cls.archetype].build()

        # Determine method for generating character stats
        print("How would you like to determine your stats? a) roll for them, or b) standard array numbers?")
        stats_choice = input("A or B: ")

        # Player chose "roll" option
        if stats_choice in ['a', "A"]:
            print("Would you like me to roll the dice or would you like to? 1) computer rolls, 2)manual entry")
            rolls = input("Who rolls? ")
            if rolls in ["1", "computer" "computer rolls"]:

                # Player chose computer rolls
                print("One moment while I roll the dice and calculate your scores.")
                assigned = cls.stats_rolled()

            elif rolls in ["2", "manual", "manual entry"]:
                # Player chose manual rolls
                assigned = cls.stats_manual_entry()

        elif stats_choice in ['b', "b"]:
            # Player chose Standard array
            assigned = cls.stats_standard_array()

        return cls(0, 0, cls.name, cls.race, 0, cls.archetype_dict[cls.archetype], **assigned)

    @classmethod
    def stats_rolled(cls):
        assigned = {}
        for s in cls.stats:
            results = []
            for d in range(4):
                roll = randint(1, 6)
                results.append(roll)
            if len(results) == 4:
                results.remove(min(results))
            assigned[s] = sum(results)
        return assigned

    @classmethod
    def stats_manual_entry(cls):
        assigned = {}
        print("Roll 4 d6 and add the three highest rolls. Do this 6 times, and jot down the numbers.")
        for stat in cls.stats:
            print("What did you roll for %s " % stat)
            val = int(input("? "))
            assigned[stat] = val
        return assigned

    @classmethod
    def stats_standard_array(cls):
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
        return assigned

    @classmethod
    def determine_modifiers(cls, stat):
        stat = stat
        cls.stat_modifier = 0
        cls.stat_modifier = (stat - 10) // 2
        return cls.stat_modifier

    def determine_saving_throws(self):
        pass

    def __repr__(self):
        return f"""Character Stats
                Name:   {self.name.capitalize()}
                Race:   {self.race.capitalize()}
                Class:  {self.archetype.capitalize()}

                STR:    {self.base_strength} + {self.races_dict[self.race.lower()].racial_str_bonus} = {self.strength}
                DEX:    {self.base_dexterity} + {self.races_dict[self.race.lower()].racial_dex_bonus} = {self.dexterity}
                CONST:  {self.base_constitution} + {self.races_dict[self.race.lower()].racial_const_bonus} = {self.constitution}
                INT:    {self.base_intelligence} + {self.races_dict[self.race.lower()].racial_int_bonus} = {self.intelligence}
                WIS:   {self.base_wisdom} + {self.races_dict[self.race.lower()].racial_wis_bonus} = {self.wisdom}
                CHAR:   {self.base_charisma} + {self.races_dict[self.race.lower()].racial_char_bonus} = {self.charisma}

                Racial Bonuses
                STR bonus:      {self.races_dict[self.race.lower()].racial_str_bonus}
                DEX bonus:      {self.races_dict[self.race.lower()].racial_dex_bonus}
                CONST bonus:    {self.races_dict[self.race.lower()].racial_const_bonus}
                INT bonus:      {self.races_dict[self.race.lower()].racial_int_bonus}
                WIS bonus:     {self.races_dict[self.race.lower()].racial_wis_bonus}
                CHAR bonus:     {self.races_dict[self.race.lower()].racial_char_bonus}

                Skill Check Modifiers
                STR:    {self.strength_modifier}
                DEX:    {self.dexterity_modifier}
                CONST:  {self.constitution_modifier}
                INT:    {self.intelligence_modifier}
                WIS:    {self.wisdom_modifier}
                CHAR:   {self.charisma_modifier}    

                Class/Archetype: {self.archetype}    
            """
