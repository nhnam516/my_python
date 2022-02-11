#npc: nhnam_testBoss
import random

listPokes = ["Kyogre", "Swampert", "Greninja", "Clefable", "Blaziken", "Palkia"]
listNature = [Nature.Modest, Nature.Adamant, Nature.Naive, Nature.Timid, Nature.Jolly, Nature.Modest]
listAbility = ["Drizzle", "Torrent", "Protean", "Unaware", "Speed Boost", "Pressure"]
listMoves = [
    ("Origin Pulse", "Thunder", "Ice Beam", "Hidden Power [Grass]"),
    ("Waterfall", "Earthquake", "Ice Punch", "Power-Up Punch"),
    ("Ice Beam", "Gunk Shot", "Low Kick", "Hidden Power [Grass]"),
    ("Moonblast", "Flamethrower", "Ice Beam", "Thunderbolt"),
    ("Flare Blitz", "High Jump Kick", "Thunder Punch", "Hidden Power [ice]"),
    ("Spacial Rend", "Hydro Pump", "Fire Blast", "Thunderbolt")]

diff_coins = [random.randint(15000, 30000),random.randint(20000, 40000),random.randint(40000, 60000)]
diff_reward = [["Focus Sash", "Aspear Berry", "Rotom", "Alomomola", "Chatot"],
               ["Focus Sash", "Rotom", "Alomomola", "Chatot", "Life Orb"],
               ["Focus Sash", "Rotom", "Alomomola", "Chatot", "Life Orb"]]
diff_reward_amount = [[int(random.randint(3, 6)), 25, 1, 1, 1],
                      [int(random.randint(5, 11)), 1, 1, 1, 1],
                      [int(random.randint(7, 13)), 1, 1, 1, 1]]
diff_weights = [(85, 85, 5, 10, 10),(80, 10, 10, 10, 10),(60, 15, 25, 25, 15)]
testBoss_three_consecutive_wins_rewardlist = ["Rotom", "Alomomola", "Chatot", "Vulpix-Alolan"]

def define_variables(x=None):
    if x is None:
        return False
    else:
        return x

define_variables(user.vars.nhnamtestBoss_3_Consecutive_wins)
define_variables(user.vars.nhnam_testBoss)

def three_consecutive_wins():
    if user.vars.nhnamtestBoss_3_Consecutive_wins == 3:
        user.say("You have defeated me 3 times in a row on Medium or Hard difficulty")
        choice_threewins_reward_1 = user.select("I have decided to give you an extra reward.", ["Rotom", "Alomomola", "Chatot", "Vulpix-Alolan"])
        choice_threewins_reward_2 = user.select("Which do you prefer?", ["Synchronized", "Shiny"])
        if choice_threewins_reward_2[0] == 0:
            choice_threewins_reward_3 = user.select("Have you bring your synchronize Pokemon with you?", ["Yes.", "No."])
            if choice_threewins_reward_3[0] == 0:
                p = Pokemon(choice_threewins_reward_1[1], 25)
                user.vars.nhnamtestBoss_3_Consecutive_wins = 0
                user.battle(p)
            else:
                user.say("Come back with your synchronize Pokemon")
        else:
            p = Pokemon(choice_threewins_reward_1[1], 25)
            user.pokes.add(p)
            user.vars.nhnamtestBoss_3_Consecutive_wins = 0

def form_boss_team(choice):
    if choice == 0:
        listItem = [None, None, None, None, None, None,]
        boss_evs = [0, 0, 0, 0, 0, 0]
    elif choice == 1:
        listItem = ["Choice Specs", "Swampertite", "Expert Belt", "Choice Specs", "Choice Band", "Choice Scarf"]
        boss_evs = [252, 252, 252, 252, 252, 252]
    else:
        listItem = ["Choice Specs", "Swampertite", "Expert Belt", "Choice Specs", "Choice Band", "Choice Scarf"]
        boss_evs = [400, 400, 400, 400, 400, 400]
    for l, n, m, i, a in zip(listPokes, listNature, listMoves, listItem, listAbility):
        p = Pokemon(l, 100)
        p.ivs = [31, 31, 31, 31, 31, 31]
        p.evs = boss_evs
        p.nature = n
        p.skills = m
        p.item = i
        p.ability = a
        nhnam_testBoss.team.append(p)

#testBoss
user.say("Hey! Don't touch my back!")
if not user.vars.nhnam_testBoss:
    choice_0 = user.select("What do you want?", ["I want to battle!", "Check consecutive wins"])
    if choice_0[0] == 0:
        three_consecutive_wins()
        if user.playtime.total_seconds() / 3600 >= 300 and all(p.level >= 100 for p in user.team):
            user.say("You seem to be feeling the rhythm, are you ready to dance?")
            choice_difficulty_1 = user.select("I prepared a few teams, how difficult should it be?", ["Easy", "Medium", "Hard"])
            choice_difficulty_2 = user.select(f"Are you sure you want to challenge me on {choice_difficulty_1[1]}]?", ["Yes", "No"])
            if choice_difficulty_2[0] == 0:
                form_boss_team(choice_difficulty_1[0])
                user.vars.set("nhnam_testBoss", True, timedelta(days=12))
                user.pause()
                if choice_difficulty_1[0] == 0:
                    user.battle(nhnam_testBoss, no_exp=True)
                else:
                    user.battle(nhnam_testBoss, no_exp=True, no_items=True)

                if user.battle == 1:
                    user.say("I seem to have lost my tempo... Anyways, here is your reward: ")
                    user.money += diff_coins[choice_difficulty_1[0]]
                    user.say(f"You received {diff_coins[choice_difficulty_1[0]]} Pokedollars.")
                    user.say("Here, take this too!}")
                    reward_list = diff_reward[choice_difficulty_1[0]]
                    reward_amount = diff_reward_amount[choice_difficulty_1[0]]
                    reward = random.choices(reward_list, weights=diff_weights[choice_difficulty_1[0]], k=1)
                    reward1 = "".join(reward)
                    for k in range(len(reward_list)):
                        if reward_list[k] == reward1:
                            amount = reward_amount[k]
                            if k == 0:
                                user.item["Focus Sash"] += amount
                            elif k == 1:
                                user.items["Aspear Berry"] += amount
                            else:
                                p = Pokemon(reward_list[k], 25)
                                user.pokes.add(p)
                    user.say(f"You have obtained {amount} {reward1}.")

                    if choice_difficulty_1[0] == 1:
                        user.vars.PvECoins = str(int(user.vars.PvECoins) + 3)
                        user.say("You received 3 PVE coins.")
                        user.vars.nhnamtestBoss_3_Consecutive_wins += 1
                        user.pause()
                        three_consecutive_wins()
                    elif choice_difficulty_1[0] == 2:
                        user.vars.PvECoins = str(int(user.vars.PvECoins) + 5)
                        user.say("You received 5 PVE coins.")
                        user.vars.nhnamtestBoss_3_Consecutive_wins += 1
                        user.pause()
                        three_consecutive_wins()
                    user.say("Goodbye.")
                else:
                    user.say(
                        "You still have a lot to learn before you can feel the beat. "
                        "Keep on practicing and you will finally make it.")
                    user.vars.nhnamtestBoss_3_Consecutive_wins = 0
            else:
                user.say("Get off!")
        else:
            user.say("You are not ready to feel the rhythm, come back when the music flows through you.")
    else:
        user.say(f"You have defeated me {user.vars.nhnamtestBoss_3_Consecutive_wins} times in a row on Medium or Hard difficulty.")
else:
    user.say("Who again?")
    choice_1 = user.select("How can I help you?", ["Check cooldown", "Chcek consecutive wins"])
    if choice_1[0] == 0:
        period = datetime.now() - nhnam_testBoss.last_fight
        user.say(f"I'm busy now... Come back in {period.days}")
    else:
        user.say(f"You have defeated me {user.vars.nhnamtestBoss_3_Consecutive_wins} times in a row on Medium or Hard difficulty.")

return