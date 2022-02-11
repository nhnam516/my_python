class Type_eff:
    def __init__(self, type):
        self.type = type

    type_list = ("normal", "fire", "water", "grass", "electric", "ice", "fighting",
                 "poison", "ground", "flying", "psychic", "bug", "rock", "ghost",
                 "dragon", "dark", "steel", "fairy")
    effect_words = ("Regular", "Effective", "Super effective", "Ineffective", "Super ineffective", "Immune")

    def check_effectiveness(x):
        if x in list(range(6)):
            while x != 10:
                return Type_eff.effect_words[x]
                x = 10

for i in Type_eff.type_list:
    if i == "normal":
        for j in Type_eff.type_list:
            if j in ("rock", "steel"):
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(3)}")
            elif j in ("ghost"):
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(5)}")
            else:
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(0)}")
    if i == "fire":
        for j in Type_eff.type_list:
            if j in ("fire", "water", "rock", "dragon"):
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(3)}")
            elif j in (""):
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(5)}")
            elif j in ("grass", "ice", "bug", "steel"):
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(1)}")
            else:
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(0)}")
    if i == "water":
        for j in Type_eff.type_list:
            if j in ("water", "grass", "dragon"):
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(3)}")
            elif j in (""):
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(5)}")
            elif j in ("fire", "ground", "rock"):
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(1)}")
            else:
                print(f"{i} against {j} is: {Type_eff.check_effectiveness(0)}")
    if i == "grass":
        for j in Type_eff.type_list:
            if j in ("fire", "grass", "poison", "flying", "bug", "dragon", "steel"):
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(3)}")
            elif j in (""):
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(5)}")
            elif j in ("water", "ground", "rock"):
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(1)}")
            else:
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(0)}")
    if i == "electric":
        for j in Type_eff.type_list:
            if j in ("grass", "electric", "dragon"):
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(3)}")
            elif j in ("ground"):
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(5)}")
            elif j in ("water", "flying"):
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(1)}")
            else:
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(0)}")
    if i == "ice":
        for j in Type_eff.type_list:
            if j in ("fire", "water", "ice", "steel"):
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(3)}")
            elif j in (""):
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(5)}")
            elif j in ("ground", "flying", "dragon"):
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(1)}")
            else:
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(0)}")
    if i == "fighting":
        for j in Type_eff.type_list:
            if j in ("poison", "flying", "psychic", "bug", "fairy"):
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(3)}")
            elif j in ("ghost"):
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(5)}")
            elif j in ("normal", "ice", "rock", "dark", "steel"):
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(1)}")
            else:
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(0)}")
    if i == "poison":
        for j in Type_eff.type_list:
            if j in ("poison", "ground", "rock", "ghost"):
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(3)}")
            elif j in ("steel"):
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(5)}")
            elif j in ("grass", "fairy"):
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(1)}")
            else:
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(0)}")
    if i == "ground":
        for j in Type_eff.type_list:
            if j in ("grass", "bug"):
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(3)}")
            elif j in ("flying"):
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(5)}")
            elif j in ("fire", "electric", "poison", "rock", "steel"):
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(1)}")
            else:
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(0)}")
    if i == "flying":
        for j in Type_eff.type_list:
            if j in ("electric", "rock", "steel"):
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(3)}")
            elif j in (""):
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(5)}")
            elif j in ("grass", "fighting", "bug"):
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(1)}")
            else:
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(0)}")
    if i == "psychic":
        for j in Type_eff.type_list:
            if j in ("psychic", "steel"):
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(3)}")
            elif j in ("dark"):
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(5)}")
            elif j in ("fighting", "poison"):
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(1)}")
            else:
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(0)}")
    if i == "bug":
        for j in Type_eff.type_list:
            if j in ("fire", "fighting", "poison", "flying", "ghost", "steel", "fairy"):
                print( f"{i} against {j} is: {Type_eff.check_effectiveness(3)}")
            elif j in (""):
                print( f"{i} against {j} is: {Type_eff.check_effectiveness(5)}")
            elif j in ("grass", "psychic", "dark"):
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(1)}")
            else:
                print( f"{i} against {j} is: {Type_eff.check_effectiveness(0)}")
    if i == "rock":
        for j in Type_eff.type_list:
            if j in ("fighting", "ground", "steel"):
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(3)}")
            elif j in (""):
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(5)}")
            elif j in ("fire", "ice", "flying", "bug"):
                print( f"{i} against {j} is: {Type_eff.check_effectiveness(1)}")
            else:
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(0)}")
    if i == "ghost":
        for j in Type_eff.type_list:
            if j in ("dark"):
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(3)}")
            elif j in ("normal"):
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(5)}")
            elif j in ("ghost", "psychic"):
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(1)}")
            else:
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(0)}")
    if i == "dragon":
        for j in Type_eff.type_list:
            if j in ("steel"):
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(3)}")
            elif j in ("fairy"):
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(5)}")
            elif j in ("dragon"):
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(1)}")
            else:
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(0)}")
    if i == "dark":
        for j in Type_eff.type_list:
            if j in ("fighting", "dark", "fairy"):
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(3)}")
            elif j in (""):
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(5)}")
            elif j in ("psychic", "ghost"):
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(1)}")
            else:
                print( f"{i} against {j} is: {Type_eff.check_effectiveness(0)}")
    if i == "steel":
        for j in Type_eff.type_list:
            if j in ("fire", "water", "electric", "steel"):
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(3)}")
            elif j in (""):
                print( f"{i} against {j} is: {Type_eff.check_effectiveness(5)}")
            elif j in ("ice", "rock", "fairy"):
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(1)}")
            else:
                print( f"{i} against {j} is: {Type_eff.check_effectiveness(0)}")
    if i == "fairy":
        for j in Type_eff.type_list:
            if j in ("fire", "poison", "steel"):
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(3)}")
            elif j in (""):
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(5)}")
            elif j in ("fighting", "dragon", "dark"):
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(1)}")
            else:
                print (f"{i} against {j} is: {Type_eff.check_effectiveness(0)}")




