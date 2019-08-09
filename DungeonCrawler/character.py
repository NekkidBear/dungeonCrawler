from races import *
from random import randint


class BaseCharacter:
    stats = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]

    def __init__(self, x, y, name, race, xp, level, hp, archetype, strength, dexterity, constitution, intelligence,
                 wisdom, charisma,  racial_str_bonus, racial_dex_bonus, racial_const_bonus, racial_int_bonus,
                 racial_wis_bonus, racial_char_bonus, skills=None):
        self.x = x
        self.y = y
        self.name = name
        self.race = race
        self.xp = xp
        self.level = level
        self.hp = hp
        self.strength = strength + racial_str_bonus
        self.dexterity = dexterity + racial_dex_bonus
        self.constitution = constitution + racial_const_bonus
        self.intelligence = intelligence + racial_int_bonus
        self.wisdom = wisdom + racial_wis_bonus
        self.charisma = charisma + racial_char_bonus
        self.racial_str_bonus = racial_str_bonus
        self.racial_dex_bonus = racial_dex_bonus
        self.racial_const_bonus = racial_const_bonus
        self.racial_int_bonus = racial_int_bonus
        self.racial_wis_bonus = racial_wis_bonus
        self.racial_char_bonus = racial_char_bonus
        self.archetype = archetype
        self.skills = skills
        self.strength_modifier = self.determine_modifiers(self.strength)
        self.dexterity_modifier = self.determine_modifiers(self.dexterity)
        self.intelligence_modifier = self.determine_modifiers(self.intelligence)
        self.wisdom_modifier = self.determine_modifiers(self.wisdom)
        self.charisma_modifier = self.determine_modifiers(self.charisma)
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
        print(", ".join(races_constant))
        cls.race = input("Race: ")
        if cls.race not in races_constant:
            print("I'm not familiar with that race. Pick from " + ", ".join(races_constant))
            print("Who are your people?")
            cls.race = input("Race: ")
        get_racial_bonus(cls.race)
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
        return cls(0, 0, cls.name, cls.race, 0, 1, 0, cls.archetype,  **assigned)

    @classmethod
    def determine_modifiers(cls, stat):
        stat = stat
        stat_modifier = 0
        if stat >= 30:
            stat_modifier = +10
        elif stat in [28, 29]:
            stat_modifier = +9
        elif stat in [26, 27]:
            stat_modifier = +8
        elif stat in [24, 25]:
            stat_modifier = +7
        elif stat in [22, 23]:
            stat_modifier = +6
        elif stat in [20, 21]:
            stat_modifier = +5
        elif stat in [18, 19]:
            stat_modifier = +4
        elif stat in [16, 17]:
            stat_modifier = +3
        elif stat in [14, 15]:
            stat_modifier = +2
        elif stat in [12, 13]:
            stat_modifier = +1
        elif stat in [10, 11]:
            stat_modifier = 0
        elif stat in [8, 9]:
            stat_modifier = -1
        elif stat in [6, 7]:
            stat_modifier = -2
        elif stat in [4, 5]:
            stat_modifier = -3
        elif stat in [2, 3]:
            stat_modifier = -4
        else:
            stat_modifier = -5
        return stat_modifier

    @classmethod
    def determine_saving_throws(cls):
        pass

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

        Racial Bonuses
        STR bonus:      {self.racial_str_bonus}
        DEX bonus:      {self.racial_dex_bonus}
        CONST bonus:    {self.racial_const_bonus}
        INT bonus:      {self.racial_int_bonus}
        WISD bonus:     {self.racial_wis_bonus}
        CHAR bonus:     {self.racial_char_bonus}
"""
