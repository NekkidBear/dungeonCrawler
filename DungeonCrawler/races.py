races_str_constant = """
1)  Dragon-Born
2)  Dwarf
3)  Elf
4)  Gnome
5)  Half-Elf
6)  Halfling
7)  Half-Orc
8)  Human
9)  Tiefling
"""


class Race:
    def __init__(self, race):
        self.name = race
        self.racial_str_bonus = 0
        self.racial_dex_bonus = 0
        self.racial_int_bonus = 0
        self.racial_const_bonus = 0
        self.racial_wis_bonus = 0
        self.racial_char_bonus = 0

    @classmethod
    def build(cls):
        pass


class DragonBorn(Race):
    def __init__(self):
        super().__init__(self)

        self.name = "Dragon-Born"
        self.racial_str_bonus = +2
        self.racial_char_bonus = +1


class Dwarf(Race):
    def __init__(self):
        super().__init__(self)
        self.name = "Dwarf"
        self.racial_const_bonus = +2


class Elf(Race):
    def __init__(self):
        super().__init__(self)
        self.name = "Elf"
        self.racial_dex_bonus = +2


class Gnome(Race):
    def __init__(self):
        super().__init__(self)
        self.name = "Gnome"
        self.racial_int_bonus = +2


class HalfElf(Race):
    def __init__(self):
        super().__init__(self)
        self.name = "Half-Elf"
        self.racial_char_bonus = +2
        self.choice_1 = ""
        self.choice_2 = ""

    @classmethod
    def build(cls):
        print("Half-Elves get to choose two stats to boost in addition to their charisma. "
              "Which two stats would you like to enhance?")
        print("""
        1) Strength
        2) Dexterity
        3) Constitution
        4) Intelligence
        5) Wisdom
        """)
        cls.choice_1 = input("Choice 1: ")
        cls.choice_2 = input("Choice 2: ")
        if cls.choice_1.lower() in ["1", "strength"] or cls.choice_2.lower() in ["1", "strength"]:
            cls.racial_str_bonus = +1
        elif cls.choice_1.lower() in ["2", "dexterity"] or cls.choice_2.lower() in ["2", "dexterity"]:
            cls.racial_dex_bonus = +1
        elif cls.choice_1.lower() in ["3", "constitution"] or cls.choice_2.lower() in ["3", "constitution"]:
            cls.racial_const_bonus = +1
        elif cls.choice_1.lower() in ["4", "intelligence"] or cls.choice_2.lower() in ["4", "intelligence"]:
            cls.racial_int_bonus = +1
        elif cls.choice_1.lower() in ["5", "wisdom"] or cls.choice_2.lower() in ["5", "wisdom"]:
            cls.racial_wis_bonus = +1


class Halfling(Race):
    def __init__(self):
        super().__init__(self)
        self.name = "Halfling"
        self.racial_dex_bonus = +2


class HalfOrc(Race):
    def __init__(self):
        super().__init__(self)
        self.name = "Half-Orc"
        self.racial_str_bonus = +2
        self.racial_const_bonus = +1


class Human(Race):
    def __init__(self):
        super().__init__(self)
        self.name = "Human"
        self.racial_str_bonus = +1
        self.racial_dex_bonus = +1
        self.racial_int_bonus = +1
        self.racial_const_bonus = +1
        self.racial_wis_bonus = +1
        self.racial_char_bonus = +1


class Tiefling(Race):
    def __init__(self):
        super().__init__(self)
        self.name = "Tiefling"
        self.racial_int_bonus = +1
        self.racial_char_bonus = +2
