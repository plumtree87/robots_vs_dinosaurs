


class Dinosaurs:
    def __init__(self):
        self.type = ''
        self.health = 100
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
            self.health += 50
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
        self.health = 50
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
            self.health += 80
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
            print("Round: ", rounds)
            print("Time to ENGAGE")
            robo1 = players_army.fleet[0]
            robo2 = players_army.fleet[1]
            robo3 = players_army.fleet[2]
            dino1 = enemies_army.herd[0]
            dino2 = enemies_army.herd[1]
            dino3 = enemies_army.herd[2]
            print("You must choose WHO to attack and WITH WHOM you will attack. Example, aa for", robo1, "to attack", dino1)
            print("or typing ab would have", dino1, "be attacked by", robo2, "Just remember, WHO WHOM")
            while robo1.health > 1 and robo2.health > 1 && robo3.health > 1 or dino1.health > 1 and dino2.health > 1 and dino3.health > 1:
                print("______________________Round:", rounds, "!!!FIGHT!!____________________________________")
                print("a: attack", dino1.type, dino1.health, "     |", "name: ", robo1.name, robo2.name, robo3.name)
                print("b: attack", dino2.type, dino2.health, "            |", "HP:    ", robo1.health, "     ", robo2.health, "     ", robo3.health)
                print("c: attack", dino3.type, dino3.health, "     |", "energy:", robo1.power_level, "     ", robo2.power_level, "   ", robo3.power_level)
                print("_____________________________________________________________________________")
                kill = input(" ")
                rounds += 1
                if kill == "aa":
                    print(robo1.name, "attacks", dino1.name, "with his", robo1.weapon, "dealing", robo1.attack_power, "damage!")
                    dino1.health -= robo1.attack_power
                    robo1.energy -= 10
                    print(dino1, "Rams you in self-defense! You receive,", dino1.attack_power,"damage!")
                    robo1.health -= dino1.attack_power
                if kill == "ab":
                    print(robo2.name, "attacks", dino1.name, "with his", robo2.weapon, "dealing", robo1.attack_power, "damage!")
                    print(dino1, "Rams you in retaliation! You receive", dino1.attack_power,"damage!")
                    



            return False

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
                    print("a:", players_army[0].name, "b:", players_army[1].name, "or, c:", players_army[2].name)
                    bot_choice = input("?")
                    if bot_choice == "a":
                        players_army[0].attack_power += 15
                        players_army[0].power_level += 100
                        players_army[0].health += 100
                        print(players_army[0].name, "feels a surge of power!")
                        print("You better get moving! Commander says hurry up!")
                        return self.area3
                    if bot_choice == "b":
                        players_army[1].attack_power += 15
                        players_army[1].power_level += 100
                        players_army[1].health += 100
                        print(players_army[1].name, "feels a surge of power!")
                        print("You better get moving! Commander says hurry up!")
                        return self.area3
                    if bot_choice == "c":
                        players_army[2].attack_power += 15
                        players_army[2].power_level += 100
                        players_army[2].health += 100
                        print(players_army[2].name, "feels a surge of power!")
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