from random import randint
from character import BaseCharacter


class Archetype:
    def __init__(self):
        self.name = ""
        self.career_level = 1
        self.hp = 0
        self.hit_dice = 0
        self.proficiencies = {}
        self.saving_throws = {}
        self.skills = {}
        self.career_equipment = {}
        self.spell_slots = {}
        self.cantrips = None

    @classmethod
    def build(cls):
        pass


class Cleric(Archetype):
    def __init__(self):
        super().__init__()
        self.name = "Cleric"
        self.career_level = 1
        self.hp = 0
        self.proficiencies = {"Armor": ["light armor", "medium armor", "shields"], "Weapons": "simple"}
        self.saving_throws = {"wisdom", "charisma"}
        self.skills = []
        self.spell_slots = {}
        self.cantrips = {}

    @classmethod
    def build(cls):
        if super().career_level == 1:
            cls.hp = 8 + constitution_modifier
        else:
            cls.hp += (randint(1, 8) + constitution_modifier) * super().career_level
        cls.skills_list = ["history", "insight", "medicine", "persuasion", "religion"]
        print("Choose two proficiency skills from the following list:")
        for i in range(len(cls.skills_list)):
            print(i, cls.skills_list[i])
        super().skills.update(input("Choice 1:"))
        super().skills.update(input("Choice 2:"))
        super().career_equipment = {"mace"}
        return cls.hp

    @classmethod
    def available_spell_slots_per_career_level(cls):
        cls.spell_slot_table = {"1": {"Cantrips": 2, "Level 1": 2},
                                "2": {"Cantrips": 2, "Level 1": 3},
                                "3": {"Cantrips": 2, "Level 1": 4, "Level 2": 3},
                                "4": {"Cantrips": 2, "Level 1": 4, "Level 2": 3},
                                "5": {"Cantrips": 2, "Level 1": 4, "Level 2": 3, "Level 3": 2},
                                "6": {"Cantrips": 2, "Level 1": 4, "Level 2": 3, "Level 3": 3},
                                "7": {"Cantrips": 2, "Level 1": 4, "Level 2": 3, },
                                "8": {"Cantrips": 2, "Level 1": 4, "Level 2": 3, },
                                "9": {"Cantrips": 2, "Level 1": 4, "Level 2": 3, },
                                "10": {"Cantrips": 2, "Level 1": 4, "Level 2": 3, },
                                "11": {"Cantrips": 2, "Level 1": 4, "Level 2": 3, },
                                "12": {"Cantrips": 2, "Level 1": 4, "Level 2": 3, },
                                "13": {"Cantrips": 2, "Level 1": 4, "Level 2": 3, },
                                "14": {"Cantrips": 2, "Level 1": 4, "Level 2": 3, },
                                "15": {"Cantrips": 2, "Level 1": 4, "Level 2": 3, },
                                "16": {"Cantrips": 2, "Level 1": 4, "Level 2": 3, },
                                "17": {"Cantrips": 2, "Level 1": 4, "Level 2": 3, },
                                "18": {"Cantrips": 2, "Level 1": 4, "Level 2": 3, },
                                "19": {"Cantrips": 2, "Level 1": 4, "Level 2": 3, },
                                "20": {"Cantrips": 2, "Level 1": 4, "Level 2": 3, }
                                }

        pass


class Rogue(Archetype):
    def __init__(self):
        super().__init__()
        pass


class Wizard(Archetype):
    def __init__(self):
        super().__init__()
        pass


class Barbarian(Archetype):
    def __init__(self):
        super().__init__()
        pass


class Ranger(Archetype):
    def __init__(self):
        super().__init__()
        pass


class Paladin(Archetype):
    def __init(self):
        super().__init__()
        pass
