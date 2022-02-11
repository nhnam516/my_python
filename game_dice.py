import time
import random
import Characters
import sys

#Not Fully random (shld be random num saved into a var, doesnt gen another ran num)

timeset = 0.5
user = Characters.Player("Lhy",20,100)
monster = Characters.Monster("Warewolf",30,100)
max_userhp = user1.hp
max_monhp = wolf1.hp

def check_input():
    user_input = input("Throw a dice? (Yes/No): ")
    if user_input.lower() == "no":
        return -1
    elif user_input.lower() == "yes":
        return 1
    else:
        return 0

def throw_dice():
    global monster_num, user_num
    monster_num = random.randrange(1, 7)
    user_num = random.randrange(1, 7)
    throw_script = []
    script1 = f"You are throwing a 6-faces dice..."
    script2 = f"You got a {user_num}!"
    script3 = f"{monster.name} is throwing his dice..."
    script4 = f"{monster.name} gets a {monster_num}!"
    throw_script.append(script1)
    throw_script.append(script2)
    throw_script.append(script3)
    throw_script.append(script4)
    for i in throw_script:
        print(i)
        time.sleep(timeset)

def Throw_true():
        if user_num == monster_num:
            time.sleep(timeset)
            pass
        elif monster_num < user_num:
            monster.hp -= user.atk
            print(f"You hit the {monster.name}! It lost {user.atk} hp!")
            time.sleep(timeset)
            if monster.hp>=0:
                print(f"{monster.name}'s current hp is {monster.hp}/{max_monhp}")
            else:
                print(f"{monster.name}'s current hp is 0/{max_monhp}")
                print("You killed it!")
                sys.exit()
            time.sleep(timeset)
        else:
            user.hp -= monster.atk
            print(f"You get hit and lost {monster.atk} hp!")
            time.sleep(timeset)
            if user.hp>=0:
                print(f"{user.name}'s current hp is {user.hp}/{max_monhp}")
            else:
                print(f"{user.name}'s current hp is 0/{max_monhp}")
                print("You get killed!")
                sys.exit()
            time.sleep(timeset)

def Dice_match(y):
    while user.hp > 0 and monster.hp > 0:
        while y == 0:
            print("This is neither 'Yes' nor 'No'!")
            y = check_input()
        while y == -1:
            time.sleep(timeset)
            print("You dropped the dice and tried to escape!")
            escape_var = random.randrange(1, 5)
            time.sleep(timeset)
            if escape_var == 2:
                print("You escaped successfully!")
                time.sleep(timeset)
                sys.exit()
            else:
                user.hp -= monster.atk
                print(f"You failed to escape! The {monster.name} attacked you! You lost {monster.atk} hp.")
                time.sleep(timeset)
                if user.hp >= 0:
                    print(f"{user.name}'s current hp is {user.hp}/{max_monhp}")
                else:
                    print(f"{user.name}'s current hp is 0/{max_monhp}")
                    print(f"Coward! You get killed!")
                    sys.exit()
                y = check_input()
        while y == 1:
            throw_dice()
            Throw_true()
            y = check_input()

x = check_input()
Dice_match(x)