from random import randint
from character import BaseCharacter


class Archetype:
    def __init__(self):
        self.name = None
        self.career_level = 1
        self.hp = None
        self.hit_dice = None
        self.proficiencies = None
        self.saving_throws = None
        self.skills = None
        self.career_equipment = None
        self.spell_slots = None
        self.cantrips = None
        self.spells_known = None

    @classmethod
    def build(cls, career_level):
        pass

    @classmethod
    def available_spell_slots_per_career_level(cls, career_level):
        pass

    @classmethod
    def determine_hp(cls):
        pass


class Cleric(Archetype):
    def __init__(self):
        super().__init__()
        self.name = "Cleric"
        self.career_level = 1
        self.proficiency_bonus = 2
        self.domain = None
        self.hp = None
        self.proficiencies = {"Armor": ["light armor", "medium armor", "shields"], "Weapons": "simple"}
        self.saving_throws = {"wisdom", "charisma"}
        self.skills = None
        self.spell_save_dc = 8 + self.proficiency_bonus + BaseCharacter.wisdom_modifier
        self.spell_attack_modifier = self.proficiency_bonus + BaseCharacter.wisdom_modifier
        self.spell_slots = None

    @classmethod
    def build(cls, career_level):
        cls.career_level = career_level
        cls.hp = cls.determine_hp()
        cls.domain = cls.domain_choice()
        cls.skills = cls.proficiency_skills_choice()
        cls.spell_slots = cls.available_spell_slots_per_career_level(cls.career_level)
        cls.career_equipment = {"mace": 1, "scale mail": 1, "light crossbow": 1, "crossbow bolts": 20,
                                "priest's pack": 1, "shield": 1, "holy symbol": 1}
        cls.cantrips = cls.cantrips_per_career_level(cls.career_level)

    @classmethod
    def determine_hp(cls):
        if super().career_level == 1:
            cls.hp = 8 + BaseCharacter.constitution_modifier
        else:
            cls.hp += (randint(1, 8) + BaseCharacter.constitution_modifier) * super().career_level
        return cls.hp

    @classmethod
    def proficiency_skills_choice(cls):
        cls.skills = []
        cls.skills_list = ["history", "insight", "medicine", "persuasion", "religion"]
        print("Choose two proficiency skills from the following list:")
        for i in range(len(cls.skills_list)):
            print(i, cls.skills_list[i])
        super().skills.update(input("Choice 1:"))
        super().skills.update(input("Choice 2:"))
        return cls.skills

    @classmethod
    def domain_choice(cls):
        cls.domain = None
        cleric_domains = ["knowledge", "life", "light", "nature", "tempest", "trickery", "war"]
        print("Choose a divine domain: ")
        for i in range(len(cleric_domains)):
            print(i, cleric_domains[i])
        cls.domain = input("Choice: ")
        return cls.domain

    @classmethod
    def domain_feature_upgrades(cls, career_level):
        cls.career_level = career_level
        if cls.career_level >= 1:
            cls.domain_choice()

    @classmethod
    def spell_book(cls, career_level):
        cls.spells_known = []
        cls.career_level = career_level
        if cls.career_level == 1:
            print("choose 2 spells")
        elif cls.career_level in [2, 6, 8, 17]:
            print("Choose a domain spell")

    @classmethod
    def cantrips_per_career_level(cls, career_level):
        cls.cantrips = []
        cls.career_level = career_level
        if cls.career_level == 1:
            print("choose 3 cantrips")
        elif cls.career_level in [4, 10]:
            print("choose a cantrip")
        return cls.cantrips

    @classmethod
    def available_spell_slots_per_career_level(cls, career_level):
        cls.career_level = career_level
        cls.character_slots = {"1st level": 2}
        cls.proficiency_bonus = +2
        if cls.career_level >= 2:
            cls.character_slots["1st level"] = 3
        if cls.career_level >= 3:
            cls.character_slots["1st level"] = 4
            cls.character_slots["2nd level"] = 2
        if cls.career_level >= 4:
            cls.character_slots["2nd level"] = 3
        if cls.career_level >= 5:
            cls.character_slots["3rd level"] = 2
        if cls.career_level >= 6:
            cls.character_slots["3rd level"] = 3
        if cls.career_level >= 7:
            cls.character_slots["4th level"] = 1
        if cls.career_level >= 8:
            cls.character_slots["4th level"] = 2
        if cls.career_level >= 9:
            cls.character_slots["4th level"] = 3
            cls.character_slots["5th level"] = 1
        if cls.career_level >= 10:
            cls.character_slots["5th level"] = 2
        if cls.career_level >= 11:
            cls.character_slots["6th level"] = 1
        if cls.career_level >= 13:
            cls.character_slots["7th level"] = 1
        if cls.career_level >= 15:
            cls.character_slots["8th level"] = 1
        if cls.career_level >= 17:
            cls.character_slots["9th level"] = 1
        if cls.career_level >= 19:
            cls.character_slots["6th level"] = 2
        if cls.career_level >= 20:
            cls.character_slots["7th level"] = 2
        return cls.character_slots

    @classmethod
    def upgrades_per_level(cls, career_level):
        cls.career_level = career_level
        return None
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
