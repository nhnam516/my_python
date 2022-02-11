#npc: testBoss

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
    ("Spacial Rend", "Hydro Pump", "Fire Blast", "Thunderbolt")
]

try:
    user.vars.wins = user.vars.wins
except:
    user.vars.wins = 0

try:
    user.vars.testBoss = user.vars.testBoss
except:
    user.vars.testBoss = False

def three_consecutive_wins():
    if user.vars.wins == 3:
        user.select("You have defeated me 3 times in a row on Medium or Hard difficulty,"
                    "I have decided to give you an extra reward.",
                    ["Rotom", "Alomomola", "Chatot", "Vulpix-Alolan"])
        if choice[0] == 0:
            user.select("Which do you prefer?", ["Synchronized", "Shiny"])
            if choice[0] == 0:
                user.select("Have you bring your synchronize Pokemon with you?", ["Yes.", "No."])
                if choice[0] == 0:
                    p = Pokemon("Rotom", 25)
                    user.vars.wins = 0
                    user.battle(p)
                else:
                    user.say("Come back with your synchronize Pokemon")
            else:
                p = Pokemon("Rotom", 25)
                user.pokes.add(p)
                user.vars.wins = 0
        elif choice[0] == 1:
            user.select("Which do you prefer?", ["Synchronized", "Shiny"])
            if choice[0] == 0:
                user.select("Have you bring your synchronize Pokemon with you?", ["Yes.", "No."])
                if choice[0] == 0:
                    p = Pokemon("Alomomola", 25)
                    user.vars.wins = 0
                    user.battle(p)
                else:
                    user.say("Come back with your synchronize Pokemon")
            else:
                p = Pokemon("Alomomola", 25)
                user.pokes.add(p)
                user.vars.wins = 0
        elif choice[0] == 2:
            user.select("Which do you prefer?", ["Synchronized", "Shiny"])
            if choice[0] == 0:
                user.select("Have you bring your synchronize Pokemon with you?", ["Yes.", "No."])
                if choice[0] == 0:
                    p = Pokemon("Chatot", 25)
                    user.vars.wins = 0
                    user.battle(p)
                else:
                    user.say("Come back with your synchronize Pokemon")
            else:
                p = Pokemon("Chatot", 25)
                user.pokes.add(p)
                user.vars.wins = 0
        elif choice[0] == 3:
            user.select("Which do you prefer?", ["Synchronized", "Shiny"])
            if choice[0] == 0:
                user.select("Have you bring your synchronize Pokemon with you?", ["Yes.", "No."])
                if choice[0] == 0:
                    p = Pokemon("Vulpix-Alolan", 25)
                    user.vars.wins = 0
                    user.battle(p)
                else:
                    user.say("Come back with your synchronize Pokemon")
            else:
                p = Pokemon("Vulpix-Alolan", 25)
                user.pokes.add(p)
                user.vars.wins = 0


#testBoss
user.say("Hey! Don't touch my back!")
if not user.vars.testBoss:
    choice = user.select("What do you want?", ["I want to battle!", "Check consecutive wins"])
    if choice[0] == 0:
        three_consecutive_wins()
        if user.playtime.total_seconds() / 3600 >= 300 and all(p.level >= 100 for p in user.team) and user.region == region.Sinnoh:
            user.say("You seem to be feeling the rhythm, are you ready to dance?")
            user.select("I prepared a few teams, how difficult should it be?", ["Easy", "Medium", "Hard"])
            if choice[0] == 0:
                choice = user.select("Are you sure you want to challenge me on Easy?", ["Yes", "No"])
                if choice[0] == 0:
                    for l, n, m, a in zip(listPokes, listNature, listMoves, listAbility):
                        p = Pokemon(l, 100)
                        p.ivs = 31, 31, 31, 31, 31, 31
                        p.evs = 0, 0, 0, 0, 0, 0
                        p.nature = n
                        p.skills = m
                        p.ability = a
                        testBoss.team.append(p)
                    user.pause()
                    user.battle(testBoss, no_exp=True, no_items=True)
                    user.vars.set("testBoss", True, timedelta(days=12))
                    if user.battle == 1:
                        user.say("I seem to have lost my tempo... Anyways, here is your reward: ")
                        user.coins += random.randint(15000, 30000)
                        user.say(f"You received {user.coins} Pokedollars.")
                        user.say("Here, take this too!}")
                        reward_list = ["Focus Sash",  "Aspear Berry", "Rotom", "Alomomola", "Chatot"]
                        reward = random.choices(reward_list, weights=(85, 85, 5, 10, 10), k=1)
                        reward1 = "".join(reward)
                        if reward1 == "Focus Sash":
                            amount = int(random.randint(3, 6))
                            user.items["Focus Sash"] += amount
                        elif reward1 == "Aspear Berry":
                            amount = 25
                            user.items["Aspear Berry"] += 25
                        elif reward1 == "Rotom":
                            p = Pokemon("Rotom",  25)
                            amount = 1
                            user.pokes.add(p)
                        elif reward1 == "Alomomola":
                            p = Pokemon("Alomomola", 25)
                            amount = 1
                            user.pokes.add(p)
                        else:
                            p = Pokemon("Chatot", 25)
                            amount = 1
                            user.pokes.add(p)
                        user.say(f"You have obtained {amount} {reward1}.")
                        user.say("Goodbye.")
                    else:
                        user.say(
                            "You still have a lot to learn before you can feel the beat. "
                            "Keep on practicing and you will finally make it.")
                        user.vars.wins = 0
                else:
                    user.say("Get off!")

            elif choice[0] == 1:
                user.say("Are you sure you want to challenge me on Medium?", ["Yes", "No"])
                if choice[0] == 0:
                    for l, n, m, i, a in zip(listPokes, listNature, listMoves, listItem, listAbility):
                        p = Pokemon(l, 100)
                        p.ivs = 31, 31, 31, 31, 31, 31
                        p.evs = 252, 252, 252, 252, 252, 252
                        p.nature = n
                        p.skills = m
                        p.item = i
                        p.ability = a
                        testBoss.team.append(p)
                    user.pause()
                    user.battle(testBoss, no_exp=True, no_items=True)
                    user.vars.set("testBoss", True, timedelta(days=12))
                    if user.battle == 1:
                        user.say("I seem to have lost my tempo... Anyways, here is your reward: ")
                        user.pause()
                        user.coins += random.randint(20000, 40000)
                        user.say(f"You received {user.coins} Pokedollars.")
                        user.say("Here, take this too!}")
                        reward_list = ["Focus Sash", "Rotom", "Alomomola", "Chatot", "Life Orb"]
                        reward = random.choices(reward_list, weights=(80, 10, 10, 10, 10), k=1)
                        reward1 = "".join(reward)
                        if reward1 == "Focus Sash":
                            amount = int(random.randint(5, 11))
                            user.items["Focus Sash"] += amount
                        elif reward1 == "Rotom":
                            p = Pokemon("Rotom", 25)
                            amount = 1
                            user.pokes.add(p)
                        elif reward1 == "Alomomola":
                            p = Pokemon("Alomomola", 25)
                            amount = 1
                            user.pokes.add(p)
                        elif reward1 == "Chatot":
                            p = Pokemon("Chatot", 25)
                            amount = 1
                            user.pokes.add(p)
                        else:
                            amount = 1
                            user.items["Life Orb"] += 1
                        user.say(f"You have obtained {amount} {reward1}")
                        PvECoins += 5
                        user.say("You received 5 PVE coins.")
                        user.vars.wins += 1
                        three_consecutive_wins()
                        user.pause()
                        user.say("Goodbye.")
                    else:
                        user.say(
                            "You still have a lot to learn before you can feel the beat. "
                            "Keep on practicing and you will finally make it.")
                        user.vars.wins = 0
                else:
                    user.say("Get off!")
            else:
                user.say("Are you sure you want to challenge me on Hard?", ["Yes", "No"])
                if choice[0] == 0:
                    for l, n, m, i, a in zip(listPokes, listNature, listMoves, listItem, listAbility):
                        p = Pokemon(l, 100)
                        p.ivs = 31, 31, 31, 31, 31, 31
                        p.evs = 400, 400, 400, 400, 400, 400
                        p.nature = n
                        p.skills = m
                        p.item = i
                        p.ability = a
                        testBoss.team.append(p)
                    user.pause()
                    user.battle(testBoss, no_exp=True, no_items=True)
                    user.vars.set("testBoss", True, timedelta(days=12))
                    if user.battle == 1:
                        user.say("I seem to have lost my tempo... Anyways, here is your reward: ")
                        user.pause()
                        user.coins += random.randint(40000, 60000)
                        user.say(f"You received {user.coins} Pokedollars.")
                        user.say("Here, take this too!}")
                        reward_list = ["Focus Sash", "Rotom", "Alomomola", "Chatot", "Life Orb"]
                        reward = random.choices(reward_list, weights=(60, 15, 25, 25, 15), k=1)
                        reward1 = "".join(reward)
                        if reward1 == "Focus Sash":
                            amount = int(random.randint(7, 13))
                            user.items["Focus Sash"] += amount
                        elif reward1 == "Rotom":
                            p = Pokemon("Rotom", 25)
                            amount = 1
                            user.pokes.add(p)
                        elif reward1 == "Alomomola":
                            p = Pokemon("Alomomola", 25)
                            amount = 1
                            user.pokes.add(p)
                        elif reward1 == "Chatot":
                            p = Pokemon("Chatot", 25)
                            amount = 1
                            user.pokes.add(p)
                        else:
                            amount = 1
                            user.items["Life Orb"] += 1
                        user.say(f"You have obtained {amount} {reward1}")
                        PvECoins += 5
                        user.say("You received 5 PVE coins.")
                        user.vars.wins += 1
                        three_consecutive_wins()
                        user.pause()
                        user.say("Goodbye.")
                    else:
                        user.say(
                            "You still have a lot to learn before you can feel the beat. "
                            "Keep on practicing and you will finally make it.")
                        user.vars.wins = 0
                else:
                    user.say("Get off!")
        else:
            user.say("You are not ready to feel the rhythm, come back when the music flows through you.")
    else:
        user.say(f"You have defeated me {user.vars.wins} times in a row on Medium or Hard difficulty.")
else:
    user.say("Who again?")
    choice = user.select("How can I help you?", ["Check cooldown", "Chcek consecutive wins"])
    if choice[0] == 0:
        period = datetime.now() - npc.last_fight
        user.say("I'm busy now... Come back in {period.days}")
    else:
        user.say(f"You have defeated me {user.vars.wins} times in a row on Medium or Hard difficulty.")

return