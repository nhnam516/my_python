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

    def check_type(self,ineff,immune,eff):
        global list
        list = []
        for j in Type_eff.type_list:
            if j in (ineff):
                a = f"{self.type} against {j} is: Ineffective"
            elif j in (immune):
                a = f"{self.type} against {j} is: Immune"
            elif j in (eff):
                a = f"{self.type} against {j} is: Effective"
            else:
                a = f"{self.type} against {j} is: Regular"
            list.append(a)
        return list

    def type_all(self,ineff,immune,eff):
        Type_eff.check_type(self, ineff, immune, eff)

normal = Type_eff("normal")
class Normal(Type_eff):
    normal_ineff = ("rock", "steel")
    normal_immune = ("ghost")
    normal_eff = ("")
    Type_eff.check_type(normal,normal_ineff,normal_immune,normal_eff)
    def type_all():
        Type_eff.type_all(normal,Normal.normal_ineff,Normal.normal_immune,Normal.normal_eff)

fire = Type_eff("fire")
class Fire(Type_eff):
    fire_ineff = ("fire", "water", "rock", "dragon")
    fire_immune = ("")
    fire_eff = ("grass", "ice", "bug", "steel")
    Type_eff.check_type(fire,fire_ineff,fire_immune,fire_eff)
    def type_all():
        Type_eff.type_all(fire,Fire.fire_ineff,Fire.fire_immune,Fire.fire_eff)

water = Type_eff("water")
class Water(Type_eff):
    water_ineff = ("water", "grass", "dragon")
    water_immune = ("")
    water_eff = ("fire", "ground", "rock")
    Type_eff.check_type(water, water_ineff, water_immune, water_eff)
    def type_all():
        Type_eff.type_all(water,Water.water_ineff,Water.water_immune,Water.water_eff)

grass = Type_eff("grass")
class Grass(Type_eff):
    grass_ineff = ("fire", "grass", "poison", "flying", "bug", "dragon", "steel")
    grass_immune = ("")
    grass_eff = ("water", "ground", "rock")
    Type_eff.check_type(grass,grass_ineff,grass_immune,grass_eff)
    def type_all():
        Type_eff.type_all(grass, Grass.grass_ineff, Grass.grass_immune, Grass.grass_eff)

electric = Type_eff("electric")
class Electric(Type_eff):
    electric_ineff = ("grass", "electric", "dragon")
    electric_immune = ("ground")
    electric_eff = ("water", "flying")
    Type_eff.check_type(electric,electric_ineff,electric_immune,electric_eff)
    def type_all():
        Type_eff.type_all(electric, Electric.electric_ineff, Electric.electric_immune, Electric.electric_eff)

ice = Type_eff("ice")
class Ice(Type_eff):
    ice_ineff = ("fire", "water", "ice", "steel")
    ice_immune = ("")
    ice_eff = ("ground", "flying", "dragon")
    Type_eff.check_type(ice,ice_ineff,ice_immune,ice_eff)
    def type_all():
        Type_eff.type_all(ice, Ice.ice_ineff, Ice.ice_immune, Ice.ice_eff)

fighting = Type_eff("fighting")
class Fighting(Type_eff):
    fighting_ineff = ("poison", "flying", "psychic", "bug", "fairy")
    fighting_immune = ("ghost")
    fighting_eff = ("normal", "ice", "rock", "dark", "steel")
    Type_eff.check_type(fighting,fighting_ineff,fighting_immune,fighting_eff)
    def type_all():
        Type_eff.type_all(fighting, Fighting.fighting_ineff, Fighting.fighting_immune, Fighting.fighting_eff)

poison = Type_eff("poison")
class Poison(Type_eff):
    poison_ineff = ("poison", "ground", "rock", "ghost")
    poison_immune = ("steel")
    poison_eff = ("grass", "fairy")
    Type_eff.check_type(poison,poison_ineff,poison_immune,poison_eff)
    def type_all():
        Type_eff.type_all(poison, Poison.poison_ineff, Poison.poison_immune, Poison.poison_eff)

ground = Type_eff("ground")
class Ground(Type_eff):
    ground_ineff = ("grass", "bug")
    ground_immune = ("flying")
    ground_eff = ("fire", "electric", "poison", "rock", "steel")
    Type_eff.check_type(ground,ground_ineff,ground_immune,ground_eff)
    def type_all():
        Type_eff.type_all(ground, Ground.ground_ineff, Ground.ground_immune, Ground.ground_eff)

flying = Type_eff("flying")
class Flying(Type_eff):
    flying_ineff = ("electric", "rock", "steel")
    flying_immune = ("")
    flying_eff = ("grass", "fighting", "bug")
    Type_eff.check_type(flying,flying_ineff,flying_immune,flying_eff)
    def type_all():
        Type_eff.type_all(flying, Flying.flying_ineff, Flying.flying_immune, Flying.flying_eff)

psychic = Type_eff("psychic")
class Psychic(Type_eff):
    psychic_ineff = ("psychic", "steel")
    psychic_immune = ("dark")
    psychic_eff = ("fighting", "poison")
    Type_eff.check_type(psychic,psychic_ineff,psychic_immune,psychic_eff)
    def type_all():
        Type_eff.type_all(psychic, Psychic.psychic_ineff, Psychic.psychic_immune, Psychic.psychic_eff)

bug = Type_eff("bug")
class Bug(Type_eff):
    bug_ineff = ("fire", "fighting", "poison", "flying", "ghost", "steel", "fairy")
    bug_immune = ("")
    bug_eff = ("grass", "psychic", "dark")
    Type_eff.check_type(bug,bug_ineff,bug_immune,bug_eff)
    def type_all():
        Type_eff.type_all(bug, Bug.bug_ineff, Bug.bug_immune, Bug.bug_eff)

rock = Type_eff("rock")
class Rock(Type_eff):
    rock_ineff = ("fighting", "ground", "steel")
    rock_immune = ("")
    rock_eff = ("fire", "ice", "flying", "bug")
    Type_eff.check_type(rock,rock_ineff,rock_immune,rock_eff)
    def type_all():
        Type_eff.type_all(rock, Rock.rock_ineff, Rock.rock_immune, Rock.rock_eff)

ghost = Type_eff("ghost")
class Ghost(Type_eff):
    ghost_ineff = ("dark")
    ghost_immune = ("normal")
    ghost_eff = ("psychic", "ghost")
    Type_eff.check_type(ghost,ghost_ineff,ghost_immune,ghost_eff)
    def type_all():
        Type_eff.type_all(ghost, Ghost.ghost_ineff, Ghost.ghost_immune, Ghost.ghost_eff)

dragon = Type_eff("dragon")
class Dragon(Type_eff):
    dragon_ineff = ("steel")
    dragon_immune = ("fairy")
    dragon_eff = ("dragon")
    Type_eff.check_type(dragon,dragon_ineff,dragon_immune,dragon_eff)
    def type_all():
        Type_eff.type_all(dragon, Dragon.dragon_ineff, Dragon.dragon_immune, Dragon.dragon_eff)

dark = Type_eff("dark")
class Dark(Type_eff):
    dark_ineff = ("fighting", "dark", "fairy")
    dark_immune = ("")
    dark_eff = ("psychic", "ghost")
    Type_eff.check_type(dark,dark_ineff,dark_immune,dark_eff)
    def type_all():
        Type_eff.type_all(dark, Dark.dark_ineff, Dark.dark_immune, Dark.dark_eff)

steel = Type_eff("steel")
class Steel(Type_eff):
    steel_ineff = ("fire", "water", "electric", "steel")
    steel_immune = ("")
    steel_eff = ("ice", "rock", "fairy")
    Type_eff.check_type(steel,steel_ineff,steel_immune,steel_eff)
    def type_all():
        Type_eff.type_all(steel, Steel.steel_ineff, Steel.steel_immune, Steel.steel_eff)

fairy = Type_eff("fairy")
class Fairy(Type_eff):
    fairy_ineff = ("fire", "poison", "steel")
    fairy_immune = ("")
    fairy_eff = ("fighting", "dragon", "dark")
    Type_eff.check_type(fairy,fairy_ineff,fairy_immune,fairy_eff)
    def type_all():
        Type_eff.type_all(fairy, Fairy.fairy_ineff, Fairy.fairy_immune, Fairy.fairy_eff)

type_list = ("normal", "fire", "water", "grass", "electric", "ice", "fighting",
             "poison", "ground", "flying", "psychic", "bug", "rock", "ghost",
             "dragon", "dark", "steel", "fairy")
effect_words = ("Regular", "Effective", "Super effective", "Ineffective", "Super ineffective", "Immune")

def display_def(t):
    for a in range(18):
        for l in Type_eff.type_list:
            if l == t:
                return list[a]
            a += 1

result_normal = Normal.type_all
result_fire = Fire.type_all
result_water = Water.type_all
result_grass = Grass.type_all
result_electric = Electric.type_all
result_ice = Ice.type_all
result_fighting = Fighting.type_all
result_poison = Poison.type_all
result_ground = Ground.type_all
result_flying = Flying.type_all
result_psychic = Psychic.type_all
result_bug = Bug.type_all
result_rock = Rock.type_all
result_ghost = Ghost.type_all
result_dragon = Dragon.type_all
result_dark = Dark.type_all
result_steel = Steel.type_all
result_fairy = Fairy.type_all

result_atk_list = (result_normal,result_fire,result_water,result_grass,result_electric,result_ice,result_fighting,
                   result_poison,result_ground,result_flying,result_psychic,result_bug,result_rock,result_ghost,
                   result_dragon,result_dark,result_steel,result_fairy)

def display_atk(t):
    for a in range(18):
        for l in Type_eff.type_list:
            if l == t:
                return result_atk_list[a]
            a += 1

attack = input("Attacking type is: ")
defense = input("Defensing type is: ")
result = display_atk(attack)
result()

result_specific_def = display_def(defense.lower())
print(result_specific_def)

