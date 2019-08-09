races_constant = ["Dragonborn",
                  "Dwarf",
                  "Elf",
                  "Gnome",
                  "Half-elf",
                  "Halfling",
                  "Half-orc",
                  "Human",
                  "Tiefling"
                  ]


class Race:
    def __init__(self, race):
        self.name = race
        self.racial_str_bonus = 0
        self.racial_dex_bonus = 0
        self.racial_int_bonus = 0
        self.racial_const_bonus = 0
        self.racial_wis_bonus = 0
        self.racial_char_bonus = 0


class Dragonborn(Race):
    def __init__(self):
        Race(self)

        self.name = "Dragonborn"
        self.racial_str_bonus = +2
        self.racial_char_bonus = +1


class Dwarf(Race):
    def __init__(self):
        Race(self)

        self.name = "Dwarf"
        self.racial_const_bonus = +2


class Elf(Race):
    def __init__(self):
        Race(self)

        self.name = "Elf"
        self.racial_dex_bonus = +2


class Gnome(Race):
    def __init__(self):
        Race(self)
        self.name = "Gnome"
        self.racial_int_bonus = +2


class HalfElf(Race):
    def __init__(self, stat_1, stat_2):
        Race(self)
        self.name = "Half-Elf"
        self.racial_char_bonus = +2
        if stat_1 == "strength" or stat_2 == "strength":
            self.racial_str_bonus = +1
        elif stat_1 == "dexterity" or stat_2 == "dexterity":
            self.racial_dex_bonus = +1
        elif stat_1 == "intelligence" or stat_2 == "intelligence":
            self.racial_int_bonus = +1
        elif stat_1 == "constitution" or stat_2 == "constitution":
            self.racial_const_bonus = +1
        elif stat_1 == "wisdom" or stat_2 == "wisdom":
            self.racial_wis_bonus = +1


class Halfling(Race):
    def __init__(self):
        Race(self)
        self.name = "Halfling"
        self.racial_dex_bonus = +2


class HalfOrc(Race):
    def __init__(self):
        Race(self)
        self.name = "Half-Orc"
        self.racial_str_bonus = +2
        self.racial_const_bonus = +1


class Human(Race):
    def __init__(self):
        Race(self)
        self.name = "Human"
        self.racial_str_bonus = +1
        self.racial_dex_bonus = +1
        self.racial_int_bonus = +1
        self.racial_const_bonus = +1
        self.racial_wis_bonus = +1
        self.racial_char_bonus = +1


class Tiefling(Race):
    def __init__(self):
        Race(self)
        self.name = "Tiefling"
        self.racial_int_bonus = +1
        self.racial_char_bonus = +2


def get_racial_bonus(race):
    race = race
    racial_str_bonus = 0
    racial_dex_bonus = 0
    racial_int_bonus = 0
    racial_const_bonus = 0
    racial_wis_bonus = 0
    racial_char_bonus = 0
    if race == "Dragonborn":
        racial_str_bonus = Dragonborn.racial_str_bonus
        racial_char_bonus = Dragonborn.racial_char_bonus
    elif race == "Dwarf":
        racial_const_bonus = Dwarf.racial_const_bonus
    elif race == "Elf":
        racial_dex_bonus = Elf.racial_dex_bonus
    elif race == "Gnome":
        racial_int_bonus = Gnome.racial_int_bonus
    elif race == "Half-Elf":
        racial_str_bonus = HalfElf.racial_str_bonus
        racial_dex_bonus = HalfElf.racial_dex_bonus
        racial_int_bonus = HalfElf.racial_int_bonus
        racial_const_bonus = HalfElf.racial_const_bonus
        racial_wis_bonus = HalfElf.racial_wis_bonus
        racial_char_bonus = HalfElf.racial_char_bonus
    elif race == "Halfling":
        racial_dex_bonus = Halfling.racial_dex_bonus
    elif race == "Half-Orc":
        racial_str_bonus = HalfOrc.racial_str_bonus
        racial_const_bonus = HalfOrc.racial_const_bonus
    elif race == "Human":
        racial_str_bonus = Human.racial_str_bonus
        racial_dex_bonus = Human.racial_dex_bonus
        racial_int_bonus = Human.racial_int_bonus
        racial_const_bonus = Human.racial_const_bonus
        racial_wis_bonus = Human.racial_wis_bonus
        racial_char_bonus = Human.racial_char_bonus
    elif race == "Tiefling":
        racial_int_bonus = Tiefling.racial_int_bonus
        racial_char_bonus = Tiefling.racial_char_bonus
    return racial_str_bonus, racial_dex_bonus, racial_int_bonus, racial_const_bonus, racial_wis_bonus, racial_char_bonus
