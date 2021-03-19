import random


class Dinosaurs:
    def __init__(self):
        self.type = ''
        self.health = 50
        self.energy = 100
        self.attack_power = 10

    def set_dino(self, number):
        print("There are three types of Dinosaurs. Which one would you like?")
        print("(a) Triceratops: +50 health")
        print("(b) T-Rex: +15 attack power -10 health")
        print("(c) Pterodactyl: base stats, but pecks at wires and sensor devices stunning opponents 1 round.")
        choice = input("Which one do you choose?")
        if choice == "a" or choice == "A" or choice == "(a)" or choice == "(B)":
            self.type = "Triceratops"
            self.health += 30
        elif choice == "b" or choice == "B" or choice == "(B)" or choice == "(b)":
            self.type = "T-Rex"
            self.health -= 20
            self.attack_power += 15
        elif choice == "c" or choice == "C" or choice == "(C)" or choice == "(c)":
            self.type = "Pterodactyl"

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
        self.health = 30
        self.power_level = 100
        self.weapon = ''
        self.attack_power = 10

    def set_bot(self, number):
        print("There are three types of Robots. Which one would you like?")
        print("Please choose bot number", number)
        print("(a) Tank360R: +80 health +5 attack power +50 power level.")
        print("(b) DPS99R: -20 health +30 attack power")
        print("(c) RepairBot: base stats, but can heal a party member +35 health per round, if has enough power_level.")
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
            self.attack_power += 30
            self.weapon = "Rail-gun"
        elif choice == "c" or choice == "C" or choice == "(c)" or choice == "(C)":
            self.name = "RepairBot"
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
            self.attack_power += 30
            self.weapon = "Rail-gun"
        elif abc == "c" or abc == "C" or abc == "(C)" or abc == "(c)":
            self.name = "RepairBot"
            self.weapon = "monkey wrench"
        else:
            self.name = "basic bot"


class Game:
    def __init__(self):
        self.rounds = 0
        self.end = False
        self.player_race = ""

    def start(self):
        self.end = False
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
        race_choice = input("Which will you play? Robots or Dinosaurs?")
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
            print("Your fleet includes...")
            players_army = Fleet()
            players_army.set_unit(robots)
            self.player_race = "Robots"
            for units in players_army.fleet:
                print(units.name)
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
            print("Your herd includes...")
            players_army = Herd()
            players_army.set_members(dinos)
            self.player_race = "Dinosaurs"
            for units in players_army.herd:
                print(units.type)
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
            print("Example. WHO: a = ", dino1.type, "WHOM: a =", robo1.name)
            print(" ")
            while robo1.health > 1 and robo2.health > 1 and robo3.health > 1 or dino1.health > 1 and dino2.health > 1 and dino3.health > 1:
                print("______________________Round:", rounds, "___FIGHT!!___a_______b_______c________________")
                print("a: attack", dino1.type, "hp:", dino1.health, "     |", "name: ", robo1.name, robo2.name, robo3.name)
                print("b: attack", dino2.type, "hp:", dino2.health, "            |", "HP:    ", robo1.health, "     ", robo2.health, "     ", robo3.health)
                print("c: attack", dino3.type, "hp:", dino3.health, "      |", "energy:", robo1.power_level, "     ", robo2.power_level, "   ", robo3.power_level)
                print("e: rest: regain energy________________________________________________________________")
                print(" ")
                kill = input("Who do you want to attack?:  ")
                fighter = input ("With whom do you want to attack with?:  ")
                rounds += 1
                if kill == "a":
                    if dino1.type == "DEAD":
                        print("Attack someone else, this character is dead.")
                    else:
                        who = dino1
                if fighter == "a":
                    if robo1.name == "DEAD":
                        print("Attack with someone else, this character is dead.")
                    else:
                        whom = robo1
                if kill == "b":
                    if dino2.type == "DEAD":
                        print("Attack someone else, this character is dead.")
                    else:
                        who = dino2
                if fighter == "b":
                    if robo2.name == "DEAD":
                        print("Attack with someone else, this character is dead.")
                    else:
                        whom = robo2


                self.attack(who, whom)




    def attack(self, who, whom):
        p_rannum = random.randint(0, 7)
        e_rannum = random.randint(0, 7)
        if p_rannum > 2 and whom.power_level > 0 and whom.name != "DEAD":
            print(" ")
            print("[roll:", p_rannum, "success 3]")
            print(whom.name, "attacks", who.type, "with his", whom.weapon, "dealing", whom.attack_power, "damage!")
            who.health -= whom.attack_power
            whom.power_level -= 10
        elif p_rannum < 3 and whom.name != "DEAD" and whom.power_level > 0:
            print(" ")
            print("[roll:", p_rannum, "success 3]")
            print(whom.name, "attacks, but misses", who.type)
            whom.power_level -= 10
        else:
            print(" ")
            print("You are either dead, or out of energy.")
        if e_rannum > 2 and who.energy > 0 and who.type != "DEAD":
            print(" ")
            print("[enemies roll:", e_rannum, "success: 3]")
            print(who.type, "attacks you in self-defense! You receive,", who.attack_power, "damage!")
            whom.health -= whom.attack_power
            who.energy -= 10
        elif e_rannum < 3 and who.energy > 0 and who.type != "DEAD":
            print(" ")
            print("[enemies roll:", e_rannum, "success: 3]")
            print(who.type, "retaliates, but in his haste misses.")
            who.energy -= 10
        else:
            print(" ")
            print("This enemy is unable to retaliate.", "hp: ", who.health, " energy: ", who.energy)
            print("The enemy's group member siezes upon the opportunity and strikes!", whom.name, "receives 10 damage!")
            whom.health -= 10

        if who.health < 1:
            who.type = "DEAD"
            who.attack_power = 0
        if whom.health < 1:
            whom.name = "DEAD"
            who.attack_power = 0


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
            print("Your enemies include...")
            enemies_army = Herd()
            enemies_army.set_members(dinosaurs)
            for members in dinosaurs:
                print(members.type)
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
            print("Your enemies include...")
            enemies_army = Fleet()
            enemies_army.set_unit(bots)
            for units in enemies_army.fleet:
                print(units.name)
        return enemies_army


class Herd:
    def __init__(self):
        self.race = "Dinosaurs"
        self.herd = []

    def set_members(self, members):
        self.herd = members


class Fleet:
    def __init__(self):
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
                return self.area2

    def begin_journey2(self, area, players_army):
        if self.area2 == area:
            print(self.area2)
            action3 = input("directions (w and e)")
            if action3 == "look" or action3 == "l":
                print("Ooo, there is a rather large and shiny crystal jutting out of a rock here..")
                print("Just like splitting an atom, the power contained in this crystal could produce")
                special_item = input("a lot of energy by putting into your de-materializer. break it out? y or n")
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
                        robo1.health += 100
                        print(robo1.name, "feels a surge of power!")
                        print("You better get moving! Commander says hurry up!")
                        return self.area3
                    if bot_choice == "b":
                        robo2.attack_power += 15
                        robo2.power_level += 100
                        robo2.health += 100
                        print(robo2.name, "feels a surge of power!")
                        print("You better get moving! Commander says hurry up!")
                        return self.area3
                    if bot_choice == "c":
                        robo3.attack_power += 15
                        robo3.power_level += 100
                        robo3.health += 100
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
        return "battle"


class DinoBattlefield:
    def __init__(self):
        self.area1 = "You stand at the eastern end of a great valley, enemies to the far west."
        self.area2 = "You to the center of the valley, enemies in the distance to the west."
        self.area3 = "You are past the halfway point, enemies in sight to the west."


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