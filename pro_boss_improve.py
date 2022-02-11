#npc: nhnam_testBoss

import random

listPokes = ["Kyogre", "Swampert", "Greninja", "Clefable", "Blaziken", "Palkia"]
listNature = [Nature.Modest, Nature.Adamant, Nature.Naive, Nature.Timid, Nature.Jolly, Nature.Modest]
listItem = ["Choice Specs", "Swampertite", "Expert Belt", "Choice Specs", "Choice Band", "Choice Scarf"]
listAbility = ["Drizzle", "Torrent", "Protean", "Unaware", "Speed Boost", "Pressure"]
listMoves = [
    ("Origin Pulse", "Thunder", "Ice Beam", "Hidden Power [Grass]"),
    ("Waterfall", "Earthquake", "Ice Punch", "Power-Up Punch"),
    ("Ice Beam", "Gunk Shot", "Low Kick", "Hidden Power [Grass]"),
    ("Moonblast", "Flamethrower", "Ice Beam", "Thunderbolt"),
    ("Flare Blitz", "High Jump Kick", "Thunder Punch", "Hidden Power [ice]"),
    ("Spacial Rend", "Hydro Pump", "Fire Blast", "Thunderbolt")]
diff_evs = [[0, 0, 0, 0, 0, 0],[252, 252, 252, 252, 252, 252],[400, 400, 400, 400, 400, 400]]
diff_item = [[],listItem,listItem]
diff_coins = [random.randint(15000, 30000),random.randint(20000, 40000),random.randint(40000, 60000)]
diff_reward = [["Focus Sash", "Aspear Berry", "Rotom", "Alomomola", "Chatot"],
               ["Focus Sash", "Rotom", "Alomomola", "Chatot", "Life Orb"],
               ["Focus Sash", "Rotom", "Alomomola", "Chatot", "Life Orb"]]
diff_reward_amount = [[int(random.randint(3, 6)), 25, 1, 1, 1],
                      [int(random.randint(5, 11)), 1, 1, 1, 1],
                      [int(random.randint(7, 13)), 1, 1, 1, 1]]
diff_weights = [(85, 85, 5, 10, 10),(80, 10, 10, 10, 10),(60, 15, 25, 25, 15)]
diff_list = ["Easy", "Medium", "Hard"]
testBoss_three_consecutive_wins_rewardlist = ["Rotom", "Alomomola", "Chatot", "Vulpix-Alolan"]

try:
    user.vars.nhnamtestBoss_3_Consecutive_wins = user.vars.nhnamtestBoss_3_Consecutive_wins
except:
    user.vars.nhnamtestBoss_3_Consecutive_wins = 0

try:
    user.vars.nhnam_testBoss = user.vars.nhnam_testBoss
except:
    user.vars.nhnam_testBoss = False


def three_consecutive_wins():
    if user.vars.nhnamtestBoss_3_Consecutive_wins == 3:
        user.select("You have defeated me 3 times in a row on Medium or Hard difficulty,"
                    "I have decided to give you an extra reward.", ["Rotom", "Alomomola", "Chatot", "Vulpix-Alolan"])
    for i in range(len(testBoss_three_consecutive_wins_rewardlist)):
        if choice[0] == i:
            user.select("Which do you prefer?", ["Synchronized", "Shiny"])
            if choice[0] == 0:
                user.select("Have you bring your synchronize Pokemon with you?", ["Yes.", "No."])
                if choice[0] == 0:
                    p = Pokemon(testBoss_three_consecutive_wins_rewardlist, 25)
                    user.vars.nhnamtestBoss_3_Consecutive_wins = 0
                    user.battle(p)
                else:
                    user.say("Come back with your synchronize Pokemon")
            else:
                p = Pokemon(testBoss_three_consecutive_wins_rewardlist[i], 25)
                user.pokes.add(p)
                user.vars.nhnamtestBoss_3_Consecutive_wins = 0

def form_boss_team(x):
    for l, n, m, a in zip(listPokes, listNature, listMoves, listItem, listAbility):
        p = Pokemon(l, 100)
        p.ivs = 31, 31, 31, 31, 31, 31
        p.evs = diff_evs[x]
        p.nature = n
        p.skills = m
        p.item = diff_item[x]
        p.ability = a
        nhnam_testBoss.team.append(p)

#testBoss
user.say("Hey! Don't touch my back!")
if not user.vars.nhnam_testBoss:
    choice = user.select("What do you want?", ["I want to battle!", "Check consecutive wins"])
    if choice[0] == 0:
        three_consecutive_wins()
        if user.playtime.total_seconds() / 3600 >= 300 and all(p.level >= 100 for p in user.team) and user.region == region.Sinnoh:
            user.say("You seem to be feeling the rhythm, are you ready to dance?")
            user.select("I prepared a few teams, how difficult should it be?", ["Easy", "Medium", "Hard"])
            for i in range(len(diff_list)):
                if choice[0] == diff_list[i]:
                    choice = user.select(f"Are you sure you want to challenge me on {diff_list[i]}]?", ["Yes", "No"])
                    if choice[0] == "Yes":
                        form_boss_team(i)
                        user.pause()
                        if i == 0:
                            user.battle(nhnam_testBoss, no_exp=True)
                        else:
                            user.battle(nhnam_testBoss, no_exp=True, no_items=True)
                        user.vars.set("nhnam_testBoss", True, timedelta(days=12))
                        if user.battle == 1:
                            user.say("I seem to have lost my tempo... Anyways, here is your reward: ")
                            user.coins += diff_coins[i]
                            user.say(f"You received {user.coins} Pokedollars.")
                            user.say("Here, take this too!}")
                            reward_list = diff_reward[i]
                            reward_amount = diff_reward_amount[i]
                            reward = random.choices(reward_list, weights=diff_weights[i], k=1)
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
                            if i == 1:
                                user.vars.PvECoins = str(int(user.vars.PvECoins) + 3)
                                user.say("You received 3 PVE coins.")
                                user.vars.nhnamtestBoss_3_Consecutive_wins += 1
                                user.pause()
                                three_consecutive_wins()
                            elif i == 2:
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
    choice = user.select("How can I help you?", ["Check cooldown", "Chcek consecutive wins"])
    if choice[0] == 0:
        period = datetime.now() - nhnam_testBoss.last_fight
        user.say(f"I'm busy now... Come back in {period.days}")
    else:
        user.say(f"You have defeated me {user.vars.nhnamtestBoss_3_Consecutive_wins} times in a row on Medium or Hard difficulty.")

return