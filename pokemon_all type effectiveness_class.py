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
        for j in Type_eff.type_list:
            if j in (ineff):
                print(f"{self.type} against {j} is: {Type_eff.check_effectiveness(3)}")
            elif j in (immune):
                print(f"{self.type} against {j} is: {Type_eff.check_effectiveness(5)}")
            elif j in (eff):
                print(f"{self.type} against {j} is: {Type_eff.check_effectiveness(1)}")
            else:
                print(f"{self.type} against {j} is: {Type_eff.check_effectiveness(0)}")

normal = Type_eff("normal")
class Normal(Type_eff):
    normal_ineff = ("rock", "steel")
    normal_immune = ("ghost")
    normal_eff = ("")
    Type_eff.check_type(normal,normal_ineff,normal_immune,normal_eff)

fire = Type_eff("fire")
class Fire(Type_eff):
    fire_ineff = ("fire", "water", "rock", "dragon")
    fire_immune = ("")
    fire_eff = ("grass", "ice", "bug", "steel")
    Type_eff.check_type(fire,fire_ineff,fire_immune,fire_eff)

water = Type_eff("water")
class Water(Type_eff):
    water_ineff = ("water", "grass", "dragon")
    water_immune = ("")
    water_eff = ("fire", "ground", "rock")
    Type_eff.check_type(water,water_ineff,water_immune,water_eff)

grass = Type_eff("grass")
class Grass(Type_eff):
    grass_ineff = ("fire", "grass", "poison", "flying", "bug", "dragon", "steel")
    grass_immune = ("")
    grass_eff = ("water", "ground", "rock")
    Type_eff.check_type(grass,grass_ineff,grass_immune,grass_eff)

electric = Type_eff("electric")
class Electric(Type_eff):
    electric_ineff = ("grass", "electric", "dragon")
    electric_immune = ("ground")
    electric_eff = ("water", "flying")
    Type_eff.check_type(electric,electric_ineff,electric_immune,electric_eff)

ice = Type_eff("ice")
class Electric(Type_eff):
    ice_ineff = ("fire", "water", "ice", "steel")
    ice_immune = ("")
    ice_eff = ("ground", "flying", "dragon")
    Type_eff.check_type(ice,ice_ineff,ice_immune,ice_eff)

fighting = Type_eff("fighting")
class Fighting(Type_eff):
    fighting_ineff = ("poison", "flying", "psychic", "bug", "fairy")
    fighting_immune = ("ghost")
    fighting_eff = ("normal", "ice", "rock", "dark", "steel")
    Type_eff.check_type(fighting,fighting_ineff,fighting_immune,fighting_eff)

poison = Type_eff("poison")
class Poison(Type_eff):
    poison_ineff = ("poison", "ground", "rock", "ghost")
    poison_immune = ("steel")
    poison_eff = ("grass", "fairy")
    Type_eff.check_type(poison,poison_ineff,poison_immune,poison_eff)

ground = Type_eff("ground")
class Ground(Type_eff):
    ground_ineff = ("grass", "bug")
    ground_immune = ("flying")
    ground_eff = ("fire", "electric", "poison", "rock", "steel")
    Type_eff.check_type(ground,ground_ineff,ground_immune,ground_eff)

flying = Type_eff("flying")
class Flying(Type_eff):
    flying_ineff = ("electric", "rock", "steel")
    flying_immune = ("")
    flying_eff = ("grass", "fighting", "bug")
    Type_eff.check_type(flying,flying_ineff,flying_immune,flying_eff)

psychic = Type_eff("psychic")
class Psychic(Type_eff):
    psychic_ineff = ("psychic", "steel")
    psychic_immune = ("dark")
    psychic_eff = ("fighting", "poison")
    Type_eff.check_type(psychic,psychic_ineff,psychic_immune,psychic_eff)

bug = Type_eff("bug")
class Bug(Type_eff):
    bug_ineff = ("fire", "fighting", "poison", "flying", "ghost", "steel", "fairy")
    bug_immune = ("")
    bug_eff = ("grass", "psychic", "dark")
    Type_eff.check_type(bug,bug_ineff,bug_immune,bug_eff)

rock = Type_eff("rock")
class Rock(Type_eff):
    rock_ineff = ("fighting", "ground", "steel")
    rock_immune = ("")
    rock_eff = ("fire", "ice", "flying", "bug")
    Type_eff.check_type(rock,rock_ineff,rock_immune,rock_eff)

ghost = Type_eff("ghost")
class Ghost(Type_eff):
    ghost_ineff = ("dark")
    ghost_immune = ("normal")
    ghost_eff = ("psychic", "ghost")
    Type_eff.check_type(ghost,ghost_ineff,ghost_immune,ghost_eff)

dragon = Type_eff("dragon")
class Dragon(Type_eff):
    dragon_ineff = ("steel")
    dragon_immune = ("fairy")
    dragon_eff = ("dragon")
    Type_eff.check_type(dragon,dragon_ineff,dragon_immune,dragon_eff)

dark = Type_eff("dark")
class Dark(Type_eff):
    dark_ineff = ("fighting", "dark", "fairy")
    dark_immune = ("")
    dark_eff = ("psychic", "ghost")
    Type_eff.check_type(dark,dark_ineff,dark_immune,dark_eff)

steel = Type_eff("steel")
class Steel(Type_eff):
    steel_ineff = ("fire", "water", "electric", "steel")
    steel_immune = ("")
    steel_eff = ("ice", "rock", "fairy")
    Type_eff.check_type(steel,steel_ineff,steel_immune,steel_eff)

fairy = Type_eff("fairy")
class Fairy(Type_eff):
    fairy_ineff = ("fire", "poison", "steel")
    fairy_immune = ("")
    fairy_eff = ("fighting", "dragon", "dark")
    Type_eff.check_type(fairy,fairy_ineff,fairy_immune,fairy_eff)



