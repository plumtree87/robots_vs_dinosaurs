import random


class Dinosaurs:
    def __init__(self):
        self.type = ''
        self.health = 80
        self.energy = 250
        self.attack_power = 15
        self.attack1 = ""
        self.attack2 = ""

    def set_dino(self, number):
        print("There are three types of Dinosaurs. Which one would you like?")
        print(" ")
        print("(a) Triceratops: +30 health")
        print("(b) T-Rex: +25 attack power -10 health")
        print("(c) Pterodactyl: health +5 attack power +10")
        choice = input("Which one do you choose?")
        if choice == "a" or choice == "A" or choice == "(a)" or choice == "(B)":
            self.type = "Triceratops"
            self.health += 30
            self.attack1 = "Three horn jab"
            self.attack2 = "Cranial slam"
        elif choice == "b" or choice == "B" or choice == "(B)" or choice == "(b)":
            self.type = "T-Rex"
            self.health -= 10
            self.attack_power += 25
            self.attack1 = "Bite"
            self.attack2 = "Leaping foot-claw slash"
        elif choice == "c" or choice == "C" or choice == "(C)" or choice == "(c)":
            self.type = "Pterodactyl"
            self.health += 20
            self.attack_power += 15
            self.attack1 = "eye peck"
            self.attack2 = "free-falling beak stab"

    def enemy_dino(self, abc):
        if abc == "a" or abc == "A" or abc == "(a)" or abc == "(B)":
            self.type = "Triceratops"
            self.health += 50
        elif abc == "b" or abc == "B" or abc == "(B)" or abc == "(b)":
            self.type = "T-Rex"
            self.health -= 20
            self.attack_power += 15
        elif abc == "c" or abc == "C" or abc == "(C)" or abc == "(c)":
            self.type = "Pterodactyl"


class Robots:
    def __init__(self):
        self.name = ''
        self.health = 50
        self.power_level = 250
        self.weapon = ''
        self.attack_power = 10

    def set_bot(self, number):
        print("There are three types of Robots. Which one would you like?")
        print("Please choose bot number", number)
        print(" ")
        print("(a) Tank360R: +40 health +5 attack power +50 power level.")
        print("(b) DPS99R: -20 health +35 attack power")
        print("(c) RepairBot: +15 health + 15 attack power and gives team +1 health per round.")
        print(" ")
        choice = input("Which one do you choose? Select by pressing the letter of your choice.")
        if choice == "a" or choice == "A" or choice == "(a)" or choice == "(A)":
            self.name = "Tank360R"
            self.health += 40
            self.attack_power += 5
            self.power_level += 50
            self.weapon = "Sword and shield"
        elif choice == "b" or choice == "B" or choice == "(b)" or choice == "(B)":
            self.name = "DPS99R"
            self.health -= 20
            self.attack_power += 35
            self.weapon = "Rail-gun"
        elif choice == "c" or choice == "C" or choice == "(c)" or choice == "(C)":
            self.name = "RepairBot"
            self.health += 20
            self.attack_power += 15
            self.weapon = "monkey wrench"

    def enemy_bot(self, abc):
        if abc == "a" or abc == "A" or abc == "(a)" or abc == "(B)":
            self.name = "Tank360R"
            self.health += 80
            self.attack_power += 5
            self.power_level += 50
            self.weapon = "Sword and shield"
        elif abc == "b" or abc == "B" or abc == "(B)" or abc == "(b)":
            self.name = "DPS99R"
            self.health -= 20
            self.attack_power += 35
            self.weapon = "Rail-gun"
        elif abc == "c" or abc == "C" or abc == "(C)" or abc == "(c)":
            self.name = "RepairBot"
            self.weapon = "monkey wrench"
            self.health += 20
            self.attack_power += 5
        else:
            self.name = "basic bot"


class Game:
    def __init__(self):
        self.herd = ""
        self.fleet = ""
        self.rounds = 0
        self.end = False
        self.player_race = ""

    def start(self):
        self.end = False
        print(" ")
        print(
            "Long ago, when Dinosaurs walked the earth. Aliens from another planet searched the galaxy for a new home.")
        print(
            "Stumbling upon earth during their light-years of searching, they came down to inhabit the far away planet.")
        print(
            "This race was very small in size, but very advanced in technology. They couldn't protect themselves alone")
        print("So, to live on earth safely, they had to build robots, much larger in size to handle the beasts.")
        print("With what little resources they had on their ship, they began to create machines of war...")
        print(" ")
        print("Thus began, the battle of Robots vs Dinosaurs.")
        print(" ")
        race_choice = input("Which will you play? Robots or Dinosaurs?")
        print(" ")
        if race_choice == "Dinos" or race_choice == "Dinosaurs" or race_choice == "dinosaurs" or race_choice == "dinos":
            self.player_race = "Dinos"
            return race_choice
        elif race_choice == "Robots" or race_choice == "robots" or race_choice == "bots" or race_choice == "Bots":
            self.player_race = "Robots"
            return race_choice

    def assemble_army(self, race_choice):
        if race_choice == "robots" or race_choice == "Robots":
            robots = []
            robot_one = Robots()
            robot_one.set_bot(1)
            robots.append(robot_one)
            print("Alright, now choose a second bot.")
            robot_two = Robots()
            robot_two.set_bot(2)
            robots.append(robot_two)
            print("Ok, now choose your third bot.")
            robot_three = Robots()
            robot_three.set_bot(3)
            robots.append(robot_three)
            print(" ")
            print("Your fleet includes...")
            players_army = Fleet()
            players_army.set_unit(robots)
            self.player_race = "Robots"
            for units in players_army.fleet:
                print(units.name)
            self.fleet = players_army
            return players_army

        elif race_choice == "dinosaurs" or race_choice == "Dinosaurs" or race_choice == "dinos":
            dinos = []
            dino_one = Dinosaurs()
            dino_one.set_dino(1)
            dinos.append(dino_one)
            print("Alright, now choose a second dinosaur.")
            dino_two = Dinosaurs()
            dino_two.set_dino(2)
            dinos.append(dino_two)
            print("Ok, now choose your third dinosaur.")
            dino_three = Dinosaurs()
            dino_three.set_dino(3)
            dinos.append(dino_three)
            print(" ")
            print("Your herd includes...")
            players_army = Herd()
            players_army.set_members(dinos)
            self.player_race = "Dinosaurs"
            for units in players_army.herd:
                print(units.type)
            self.herd = players_army
            return players_army

    def battle_start(self, rounds, players_army, enemies_army):
            print("Time to ENGAGE")
            robo1 = players_army.fleet[0]
            robo2 = players_army.fleet[1]
            robo3 = players_army.fleet[2]
            dino1 = enemies_army.herd[0]
            dino2 = enemies_army.herd[1]
            dino3 = enemies_army.herd[2]
            print("Choose WHO to attack and WITH WHOM you will attack. You must roll over your success to succeed a hit")
            print("Example. WHO: a = ", dino1.type, "and WHOM: a =", robo1.name)
            print(" ")
            while robo1.health > 0 or robo2.health > 0 or robo3.health > 0 and dino1.health > 0 or dino2.health > 0 or dino3.health > 0:
                if robo1.health < 1 and robo2.health < 1 and robo3.health < 1:
                    print(" ")
                    print("The Dinosaurs destroy your machines, and having no mor resources for battle..")
                    print("The Commander turns the ship away from earth, and sets off to another planet to make home.")
                    print("One with far less ferocious beasts...")
                    print(
                        "Perhaps if your race wasn't only 1/2 foot tall, your 10ft gundam-style robots could have stood a chance.")
                    print("YOU LOSE~")
                    return True

                elif dino1.health < 1 and dino2.health < 1 and dino3.health < 1:
                    print(" ")
                    print("OUTSTANDING!! YOU WIN!! Despite the great disadvantage of size... your race overcame...")
                    print(
                        "and rewrote history, which isn't true in my reality, thus you are from an alternate reality.")
                    print("and the reality in which your story played, is merely a glimpse into what could have been.")
                    print("If your reality, was our reality, but alas...")
                    print(
                        "What your alternate reality in the future; this reality calls earth in english, you now call home.")
                    return True
                print("______________________Round:", rounds, "___FIGHT!!_____(a)_______(b)_______(c)________________")
                print("a: attack", dino1.type, "hp:", dino1.health, "     |", "name: ", robo1.name, robo2.name, robo3.name)
                print("b: attack", dino2.type, "hp:", dino2.health, "            |", "HP:    ", robo1.health, "     ", robo2.health, "     ", robo3.health)
                print("c: attack", dino3.type, "hp:", dino3.health, "     |", "energy:", robo1.power_level, "     ", robo2.power_level, "   ", robo3.power_level)
                print("_____________________________________________________________________________________")
                print(" ")
                enemy = input("Who do you want to attack?:")
                fighter = input("With whom do you want to attack with?:")
                rounds += 1
                if enemy == "a":
                    who = dino1
                if fighter == "a":
                    whom = robo1
                if enemy == "b":
                    who = dino2
                if fighter == "b":
                    whom = robo2
                if enemy == "c":
                    who = dino3
                if fighter == "c":
                    whom = robo3

                self.mark_death(who, whom)

    def mark_death(self, who, whom):
        if who.type == "DEAD" or whom.name == "DEAD":
            print("Sorry, but the dead cannot fight")
        else:

            if self.fleet.fleet[0].name == "RepairBot" or self.fleet.fleet[1].name == "RepairBot" or self.fleet.fleet[2].name == "RepairBot":
                if self.fleet.fleet[0].name != "DEAD":
                    self.fleet.fleet[0].health += 1
                    print("RepairBot repairs, ", self.fleet.fleet[0].name)
                if self.fleet.fleet[1].name != "DEAD":
                    self.fleet.fleet[1].health += 1
                    print("RepairBot repairs: ", self.fleet.fleet[1].name)
                if self.fleet.fleet[2].name != "DEAD":
                    self.fleet.fleet[2].health += 1
                    print("RepairBot repairs: ", self.fleet.fleet[2].name)
            self.attack(who, whom)

    def attack(self, who, whom):
        p_rannum = random.randint(0, 7)
        e_rannum = random.randint(0, 7)
        if p_rannum > 2 and whom.power_level > 0:
            print(" ")
            print("[roll:", p_rannum, "success 3]")
            print(whom.name, "attacks", who.type, "with his", whom.weapon, "dealing", whom.attack_power, "damage!")
            who.health -= whom.attack_power
            whom.power_level -= 10
        elif p_rannum < 3 and whom.power_level > 0:
            print(" ")
            print("[roll:", p_rannum, "success 3]")
            print(whom.name, "attacks, but misses", who.type)
            whom.power_level -= 10
        else:
            print(" ")
            print("You are out of energy.")
        if e_rannum > 2 and who.energy > 0:
            print(" ")
            print("[enemies roll:", e_rannum, "success: 3]")
            print(who.type, "attacks you in self-defense! You receive,", who.attack_power, "damage!")
            whom.health -= who.attack_power
            who.energy -= 10
        elif e_rannum < 3 and who.energy > 0:
            print(" ")
            print("[enemies roll:", e_rannum, "success: 3]")
            print(who.type, "retaliates, but in his haste misses.")
            who.energy -= 10
        else:
            print(" ")
            print("the enemy is out of energy")

        if who.health < 1:
            who.type = "DEAD"
        if whom.health < 1:
            whom.name = "DEAD"

    def battle_start_for_dinosaurs(self, rounds, players_army, enemies_army):
            print("Time to ENGAGE")
            dino1 = players_army.herd[0]
            dino2 = players_army.herd[1]
            dino3 = players_army.herd[2]
            robo1 = enemies_army.fleet[0]
            robo2 = enemies_army.fleet[1]
            robo3 = enemies_army.fleet[2]
            print("Choose WHO to attack and WITH WHOM you will attack. You must roll over your success to succeed a hit")
            print("Example. WHO: a = ", dino1.type, "and WHOM: a =", robo1.name)
            print(" ")
            while robo1.health > 1 or robo2.health > 1 or robo3.health > 1 and dino1.health > 1 or dino2.health > 1 or dino3.health > 1:
                if robo1.health < 1 and robo2.health < 1 and robo3.health < 1:
                    print(" ")
                    print("The Dinosaurs destroy your machines, and having no mor resources for battle..")
                    print("The Commander turns the ship away from earth, and sets off to another planet to make home.")
                    print("One with far less ferocious beasts...")
                    print("Perhaps if your race wasn't only 1/2 foot tall, your 10ft gundam-style robots could have stood a chance.")
                    print("YOU LOSE~")
                    return True

                elif dino1.health < 1 and dino2.health < 1 and dino3.health < 1:
                    print(" ")
                    print("OUTSTANDING!! YOU WIN!! Despite the great disadvantage of size... your race overcame...")
                    print(
                        "and rewrote history, which isn't true in my reality, thus you are from an alternate reality.")
                    print("and the reality in which your story played, is merely a glimpse into what could have been.")
                    print("If your reality, was our reality, but alas...")
                    print(
                        "What your alternate reality in the future; this reality calls earth in english, you now call home.")
                    return True
                print("______________________Round:", rounds, "___FIGHT!!_________________________________________")
                print("a: attack", dino1.type, "hp:", dino1.health, "     |", "name: ", "(a)", robo1.name, "(b)", robo2.name,
                      "c", robo3.name)
                print("b: attack", dino2.type, "hp:", dino2.health, "            |", "HP:    ", robo1.health, "     ",
                      robo2.health, "     ", robo3.health)
                print("c: attack", dino3.type, "hp:", dino3.health, "     |", "energy:", robo1.power_level, "     ",
                      robo2.power_level, "   ", robo3.power_level)
                print("_____________________________________________________________________________________")
                print(" ")
                enemy = input("Who do you to attack with?:")
                fighter = input("Whom do you want to attack??:")
                rounds += 1
                if enemy == "a":
                    who = dino1
                if fighter == "a":
                    whom = robo1
                if enemy == "b":
                    who = dino2
                if fighter == "b":
                    whom = robo2
                if enemy == "c":
                    who = dino3
                if fighter == "c":
                    whom = robo3

                self.mark_death_dinos(whom, who)

    def mark_death_dinos(self, whom, who):
        if who.type == "DEAD" or whom.name == "DEAD":
            print("Sorry, but the dead cannot fight")
        else:
            if whom.name == "RepairBot" and who.health < 150:
                whom.health += 15
                print(whom.name, "repairs himself regaining +15 health")
            self.attack_dinos(who, whom)

    def attack_dinos(self, whom, who):
        p_rannum = random.randint(0, 7)
        e_rannum = random.randint(0, 7)
        if p_rannum > 2 and whom.energy > 0:
            print("a :", whom.attack1)
            print("b :", whom.attack2)
            print("Which attack do you want to use?")
            attack_choice = input(" ")
            if attack_choice == "a" or attack_choice == "A":
                if whom.type == "T-Rex":
                    print(whom.type, "attacks", who.name, "with", whom.type, "and crushes,", who.name, "with his jaws!")
                    print("dealing", whom.attack_power, "damage to", who.name)
                    who.health -= whom.attack_power
                    whom.energy - 10
                if whom.type == "Triceratops":
                    tri_rannum = random.randint(0, 7)
                    if tri_rannum > 3:
                        print(whom.type, "charges in and gouges", who.name, "with a", whom.attack1, "CRITICAL HIT! 10x3 damage!")
                        who.health -= (whom.attack_power * 2)
                    else:
                        print(whom.type, "charges in and gouges", who.name, "with a", whom.attack1, "dealing 5 damage 5 damage 5 damage ")
                        who.health -= whom.attack_power
                        whom.energy -= 10
                if whom.type == "Pterodactyl":
                    print(whom.type, "gouges at the eye senors of", who.name, "giving you a chance for him to re-roll his retaliation attack!!")
                    print(" ")
                    print(who.name,"'s retaliate attack is currently [roll:", e_rannum, "success 3]")
                    r_roll = input("Do you want to roll for a chance to make enemy re-roll? y or n ")
                    if r_roll == "Y" or r_roll == "y":
                        ptero_rannum = random.randint(0, 7)
                        print("Your attempt: [roll : ", ptero_rannum, "success: 4]")
                        if ptero_rannum > 3:
                            e_rannum = random.randint(0, 7)
                            print("his new roll is:  [roll:", e_rannum, "success 3]")
                            print(' ')
                            print("*CRITICAL STRIKE* your attack dealt", whom.attack_power, "damage")
                            who.health -= whom.attack_power
                            whom.energy -= 10
                        else:
                            print("Your attack deals", (whom.attack_power - 15), "damage.")
                            who.health -= (whom.attack_power - 15)
                            whom.energy -= 10
                    else:
                        print("Your attack deals", (whom.attack_power -15), "damage.")
                        who.health -= (whom.attack_power -15)
                        whom.energy -= 10
            if attack_choice == "b" or attack_choice == "B":
                if whom.type == "T-Rex":
                    print(whom.type, "leaps into the air on", who.name, "and", whom.type, "and slashes,", who.name, "with his feet_claws.")
                    print("dealing,", whom.attack_power, "damage to", who.name)
                    who.health -= whom.attack_power
                    whom.energy - 10
                if whom.type == "Triceratops":
                    print(whom.type, "slams", who.name, "with a", whom.attack1, "dealing", whom.attack_power, "damage.")
                    who.health -= whom.attack_power
                    whom.energy -= 10
                if whom.type == "Pterodactyl":
                    print(whom.type, "flies high up into the sky, then folds his wings and free-falls quickly to the earth stabbing", who.name, "with his beak!")
                    print("dealing", whom.attack_power +5, "damage")
                    who.health -= (whom.attack_power +5)
                    whom.energy -= 10
        if p_rannum < 3 and whom.energy > 0:
            print(" ")
            print("[roll:", p_rannum, "success 3]")
            print(whom.type, "attacks, but misses", who.name)
            whom.energy -= 10
        if e_rannum > 2 and who.power_level > 0:
            print(" ")
            print("[enemies roll:", e_rannum, "success: 3]")
            print(who.name, "attacks you in self-defense! You receive,", who.attack_power, "damage!")
            whom.health -= who.attack_power
            who.power_level -= 10
        elif e_rannum < 3 and who.power_level > 0:
            print(" ")
            print("[enemies roll:", e_rannum, "success: 3]")
            print(who.name, "retaliates, but in his haste misses.")
            who.power_level -= 10
        else:
            print(" ")
            print("the enemy is out of energy")
        if who.health < 1:
            who.name = "DEAD"
        if whom.health < 1:
            whom.type = "DEAD"


    def assemble_enemies(self, race_choice):
        if race_choice == "bots" or race_choice == "robots" or race_choice == "Robots" or race_choice == "ROBOTS":
            dinosaurs = []
            dino_one = Dinosaurs()
            dino_one.enemy_dino("a")
            dinosaurs.append(dino_one)
            dino_two = Dinosaurs()
            dino_two.enemy_dino("b")
            dinosaurs.append(dino_two)
            dino_three = Dinosaurs()
            dino_three.enemy_dino("c")
            dinosaurs.append(dino_three)
            print(" ")
            print("Having run out of resources, your company must mine for ore if you want to survive...")
            print("Yet, the dinosaurs prevent you from being safe enough to even beginning to start mining.")
            print("Thus, the Commander of the ship has sent you, with all his company's resources to create that safety.")
            print("By annihilating the dinosaurs from off the face of the earth...")
            print("Your journey begins...")
            print(" ")
            print("Your enemies include...")
            enemies_army = Herd()
            enemies_army.set_members(dinosaurs)
            for members in dinosaurs:
                print(members.type)
            print(" ")
            return enemies_army

        elif race_choice == "dinosaurs" or race_choice == "DINOSAURS" or race_choice == "dinos" or race_choice == "Dinosaurs":
            bots = []
            bot_one = Robots()
            bot_one.enemy_bot("a")
            bots.append(bot_one)
            bot_two = Robots()
            bot_two.enemy_bot("b")
            bots.append(bot_two)
            bot_three = Robots()
            bot_three.enemy_bot("c")
            bots.append(bot_three)
            print(" ")
            print("Your enemies include...")
            enemies_army = Fleet()
            enemies_army.set_unit(bots)
            for units in enemies_army.fleet:
                print(units.name)
            print(" ")
        return enemies_army


class Herd:
    def __init__(self):
        self.race = "Dinosaurs"
        self.herd = []

    def set_members(self, members):
        self.herd = members


class Fleet:
    def __init__(self):
        self.race = "Robots"
        self.fleet = []

    def set_unit(self, units):
        self.fleet = units


class BotBattlefield:
    def __init__(self):
        self.area1 = "You stand at the western end of a great valley, enemies to the far east."
        self.area1a = "You stand at the western end of a great valley, enemies to the far east..."
        self.area2 = "You are past the center of the valley, enemies in the distance to the east."
        self.area2a = "You are past the center of the valley, enemies in the distance to the east..."
        self.area3 = "You are in enemy territory, enemies in sight!"

    def begin_journey(self, area, players_army):
        print(self.area1)
        if area == self.area1:
            print("type look and check your surroundings, or continue east by typing e")
            action1 = input(" ")
            if action1 == "look" or action1 == "l":
                print("There's a giant bone barely sticking out of a pool of tar here...")
                take_club = input("It might make for a very heavy hitting club... take? y or n ")
                if take_club == "y":
                    weapon = Weapon()
                    weapon.equip_club(players_army)
                    del weapon
                    print("Nothing much else in this area, directions available? e")
                    action2 = input("")
                    if action2 == "e" or action2 == "E":
                        return self.area2
                elif take_club == "n":
                    print("the giant bone begins to sink into the tar, then disappears.")
                    action2 = input("Nothing much else in the area, directions available? e ")
                    if action2 == "e" or action2 == "E":
                        return self.area2
                    else:
                        print("sorry, but the commander said go east NOW!")
                        return self.area2
            if action1 == "e" or action1 == "E" or action1 == "e" or action1 == "E":
                print("You continue eastward.")
                return self.area2

        else:
            direction = input("Directions: e")

            if direction == "e" or direction == "E" or direction == "east":
                return self.area2
            else:
                print("Commander says go EAST.")
                print(" You quickly turn back towards the battle and head east...")
                return self.area2

    def begin_journey2(self, area, players_army):
        if self.area2 == area:
            print(self.area2)
            action3 = input("directions (w and e)")
            if action3 == "look" or action3 == "l":
                print("Ooo, there is a rather large and shiny crystal jutting out of a rock here..")
                print("Just like splitting an atom, the power contained in this crystal could produce")
                special_item = input("a lot of energy by putting into your de-materializer. Use it? y or n")
                if special_item == "y" or special_item == "Y" or special_item == "yes":
                    print("You break out the crystal and need to decide which bot you want to use it.")
                    robo1 = players_army.fleet[0]
                    robo2 = players_army.fleet[1]
                    robo3 = players_army.fleet[2]
                    print("a:", robo1.name, "b:", robo2.name, "or, c:", robo3.name)
                    bot_choice = input("?")
                    if bot_choice == "a":
                        robo1.attack_power += 15
                        robo1.power_level += 100
                        robo1.health += 50
                        print(robo1.name, "feels a surge of power!")
                        print("You better get moving! Commander says hurry up!")
                        return self.area3
                    if bot_choice == "b":
                        robo2.attack_power += 15
                        robo2.power_level += 100
                        robo2.health += 50
                        print(robo2.name, "feels a surge of power!")
                        print("You better get moving! Commander says hurry up!")
                        return self.area3
                    if bot_choice == "c":
                        robo3.attack_power += 15
                        robo3.power_level += 100
                        robo3.health += 50
                        print(robo3.name, "feels a surge of power!")
                        print("You better get moving! Commander says hurry up!")
                        return self.area3
                    else:
                        print("the crystal shatters in your hands! Be more gentle next time... now get a move on")
                        return self.area3
                else:
                    print("Oh well, who cares about POWER!!! In a time like this??")
                    print("well, better get a move on...")
                    return self.area3
            if action3 == "w" or action3 == "W" or action3 == "west":
                return self.area1a
            elif action3 == "e" or action3 == "E" or action3 == "east":
                return self.area3
            else:
                print("Commander says GET A MOVE ON! You can't play around any longer, and head east.")
                return self.area3
        else:
            print("Well, it's time for battle... Commander said get going east.")
            return self.area3

    def begin_journey3(self, area, player_army):
        print(area)
        print("You come into contact with hostile, ravage, giant DINOSAURS!!!")
        print(" ")
        return "battle"


class DinoBattlefield:
    def __init__(self):
        self.area1 = "You stand at the far east of the valley, enjoying leisurely time"

    def begin_dino_journey(self):
        print("The T-Rex munches on some small sheep, the Triceratops unafraid, with the Pterodactyl flying high in the sky.")
        print("All the sudden, robots from the west come toward you and begin to battle!")
        return "battle"

class Weapon:
    def __init__(self):
        self.weapon = ""

    def equip_club(self, players_army):
        print("Only Tank360R is interested in using this...")
        for units in players_army.fleet:
            if units.name == "Tank360R":
                equip_choice = input("Would you like to equip him with it, instead of his sword? y or n ")
                if equip_choice == "y":
                    units.weapon = "giant bone maul"
                    units.attack_power += 5
                    self.weapon = "giant bone maul"
                    print("You equip a giant bone maul with Tank360R. His attack power is now:", units.attack_power, "+5")
                    break
                if equip_choice == "n":
                    break
