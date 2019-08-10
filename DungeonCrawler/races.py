races_constant = ["Dragonborn", "Dwarf", "Elf", "Gnome", "Half-Elf", "Halfling", "Half-orc", "Human", "Tiefling"]


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
        super().__init__(self)

        self.name = "Dragonborn"
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
        self.racial_str_bonus = +1
        self.racial_dex_bonus = +1
        self.racial_int_bonus = +1
        self.racial_const_bonus = +1
        self.racial_wis_bonus = +1


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


def get_racial_bonus(race, stat):
    race = race
    stat = stat
    racial_bonus = 0
    if race == "Dragonborn":
        if stat == "strength":
            racial_bonus = Dragonborn().racial_str_bonus
        elif stat == "charisma":
            racial_bonus = Dragonborn().racial_char_bonus
        else:
            pass
    elif race == "Dwarf":
        if stat == "constitution":
            racial_bonus = Dwarf().racial_const_bonus
        else:
            pass
    elif race == "Elf":
        if stat == "dexterity":
            racial_bonus = Elf().racial_dex_bonus
        else:
            pass
    elif race == "Gnome":
        if stat == "intelligence":
            racial_bonus = Gnome().racial_int_bonus
        else:
            pass
    elif race == "Half-Elf":
        if stat == "charisma":
            racial_bonus = HalfElf().racial_char_bonus
        elif stat == "strength" and (half_elf_choice_1 == "strength" or half_elf_choice_2 == "strength"):
            racial_bonus = HalfElf().racial_str_bonus
        elif stat == "dexterity" and (half_elf_choice_1 == "dexterity" or half_elf_choice_2 == "dexterity"):
            racial_bonus = HalfElf().racial_dex_bonus
        elif stat == "intelligence" and (half_elf_choice_1 == "intelligence" or half_elf_choice_2 == "intelligence"):
            racial_bonus = HalfElf().racial_int_bonus
        elif stat == "constitution" and (half_elf_choice_1 == "constitution" or half_elf_choice_2 == "constitution"):
            racial_bonus = HalfElf().racial_const_bonus
        elif stat == "wisdom" and (half_elf_choice_1 == "wisdom" or half_elf_choice_2 == "wisdom"):
            racial_bonus = HalfElf().racial_dex_bonus
        else:
            pass
    elif race == "Halfling":
        if stat == "dexterity":
            racial_bonus = Halfling().racial_dex_bonus
        else:
            pass
    elif race == "Half-Orc":
        if stat == "strength":
            racial_bonus = HalfOrc().racial_str_bonus
        elif stat == "constitution":
            racial_bonus = HalfOrc().racial_const_bonus
        else:
            pass
    elif race == "Human":
        if stat == "strength":
            racial_bonus = Human().racial_str_bonus
        elif stat == "dexterity":
            racial_bonus = Human().racial_dex_bonus
        elif stat == "constitution":
            racial_bonus = Human().racial_const_bonus
        elif stat == "intelligence":
            racial_bonus = Human().racial_int_bonus
        elif stat == "wisdom":
            racial_bonus = Human().racial_wis_bonus
        elif stat == "charisma":
            racial_bonus = Human().racial_char_bonus
        else:
            pass
    elif race == "Tiefling":
        if stat == "intelligence":
            racial_bonus = Tiefling().racial_int_bonus
        elif stat == "charisma":
            racial_bonus = Tiefling().racial_char_bonus
        else:
            pass

    return racial_bonus
