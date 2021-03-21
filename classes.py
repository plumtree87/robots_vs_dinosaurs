import random


class Dinosaurs:
    def __init__(self):
        self.type = ''
        self.health = 100
        self.energy = 250
        self.attack_power = 15
        self.attack1 = ""
        self.attack2 = ""

    def set_dino(self, number):
        print("There are three types of Dinosaurs. Which one would you like?")
        print("Please choose dino", number)
        print(" ")
        print("(a) Triceratops: +30 health and has attack moves 'Cranial Bash' and 'Tri-Horn Jab' ")
        print("(b) ___T-Rex___: +25 attack power and -10 health with attack moves 'Bite' and 'Leaping foot-claw slash' ")
        print("(c) Pterodactyl: health +5 and +10 attack power with attack moves 'eye peck' which has a chance to make")
        print("enemy retaliation attack re-roll and miss their next attack, and/or has 'free-falling beak stab'")
        print(" ")
        choice = input("Which one do you choose?")
        while choice != "a" or choice != "b" or choice != "c":
            if choice == "a" or choice == "b" or choice == "c":
                break
            else:
                choice = input("Which one do you choose? Select by pressing the letter of your choice. ")
        if choice == "a" or choice == "A" or choice == "(a)" or choice == "(B)":
            self.type = "Triceratops"
            self.health += 30
            self.attack1 = "Three horn jab"
            self.attack2 = "Cranial slam"
        elif choice == "b" or choice == "B" or choice == "(B)" or choice == "(b)":
            self.type = "___T-Rex___"
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
            self.health += 100
            self.energy += 200
        elif abc == "b" or abc == "B" or abc == "(B)" or abc == "(b)":
            self.type = "___T-Rex___"
            self.health += 15
            self.attack_power += 15
            self.energy += 200
        elif abc == "c" or abc == "C" or abc == "(C)" or abc == "(c)":
            self.type = "Pterodactyl"
            self.attack_power += 10
            self.energy += 200
            self.health += 20


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
        print("(a) _Tank360_R_: +40 health +5 attack power +50 power level.")
        print("(b) _DPS_9_9_R_: -15 health +35 attack power")
        print("(c) _Repair_Bot: +15 health + 15 attack power and gives team +1.5 health per round.")
        print(" ")
        choice = input("Which one do you choose? Select by pressing the letter of your choice.")
        while choice != "a" or choice != "b" or choice != "c":
            if choice == "a" or choice == "b" or choice == "c":
                break
            else:
                choice = input("Which one do you choose? Select by pressing the letter of your choice. ")

        if choice == "a" or choice == "A" or choice == "(a)" or choice == "(A)":
            self.name = "_Tank360_R_"
            self.health += 40
            self.attack_power += 5
            self.power_level += 50
            self.weapon = "Sword and shield"
            print(" ")
            print(self.name, "currently uses", self.weapon, "another option would be a greatsword which would give -5 health + 5 attack power")
            wep_change = input("Would you like to use the greatsword? y or press n to keep the sword and shield.")
            while wep_change != "y" or wep_change != "n":
                if wep_change == "y" or wep_change == "n":
                    break
                else:
                    wep_change = input("Would you like to use the greatsword? y or n ")
            if wep_change == "y":
                weapon = Weapon().weapon_tank_list[2]
                self.weapon = weapon
                print(self.name, "now uses a greatsword")
                self.health -= 5
                self.attack_power += 5
                print(" ")
            else:
                print(" ")
                print(self.name, "keeps the", self.weapon)
                print(" ")
        elif choice == "b" or choice == "B" or choice == "(b)" or choice == "(B)":
            self.name = "_DPS_9_9_R_"
            self.health -= 15
            self.attack_power += 35
            self.weapon = "Rail-gun"
            print(" ")
            print(self.name, "currently uses", self.weapon, "but has a few options..")
            weapon = Weapon().weapon_list
            for guns in weapon:
                print("Would you like to use", guns, "instead?")
                swap = input("y or n")
                if swap == "y":
                    self.weapon = guns
                    print(self.name, "now uses", self.weapon)
                    break
                if swap == "n":
                    continue
                while swap != "y" or swap != "n":
                    if swap == "y":
                        self.weapon = guns
                        print(self.name, "now uses,", self.weapon)
                        break
                    if swap == "n":
                        break
                    else:
                        swap = input("y or n")
            print(" ")
            print(self.name, "will use", self.weapon,"for his weapon.")
            print("he's added to your fleet now...")
            print(" ")
        elif choice == "c" or choice == "C" or choice == "(c)" or choice == "(C)":
            self.name = "_Repair_Bot"
            self.health += 20
            self.attack_power += 15
            self.weapon = "monkey wrench"
            print(" ")
            print(self.name, "currently uses", self.weapon, "which heals all party members +1.5 hp per round.")
            print("another option would be a hammer, which doesn't allow healing but deals +10 more damage")
            wep_choice = input ("Would you like to change to a hammer?: y :or keep the monkey wrench?: n ")
            while wep_choice != "y" or wep_choice != "n":
                if wep_choice == "y" or wep_choice == "n":
                    break
                else:
                    wep_choice = input("Would you like to change to hammer? y or n ")
            if wep_choice == "y":
                weapon = Weapon().weapon_repair_list[1]
                self.weapon = weapon
                self.attack_power += 10
                print(" ")
                print(self.name, "equips the", self.weapon)
                print(" ")
            else:
                print(" ")
                print(self.name, "keeps the", self.weapon)
                print(" ")

    def enemy_bot(self, abc):
        if abc == "a" or abc == "A" or abc == "(a)" or abc == "(B)":
            self.name = "_Tank360_R_"
            self.health += 80
            self.attack_power += 5
            self.power_level += 50
            self.weapon = "Sword and shield"
        elif abc == "b" or abc == "B" or abc == "(B)" or abc == "(b)":
            self.name = "_DPS_9_9_R_"
            self.health -= 20
            self.attack_power += 35
            self.weapon = "Rail-gun"
        elif abc == "c" or abc == "C" or abc == "(C)" or abc == "(c)":
            self.name = "_Repair_Bot"
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
        while self.player_race != "Dinos" or self.player_race != "Robots":
            race_choice = input("Which will you play? Robots or Dinosaurs?")
            print(" ")
            if race_choice == "Dinos" or race_choice == "Dinosaurs" or race_choice == "dinosaurs" or race_choice == "dinos":
                self.player_race = "Dinos"
                return self.player_race
            elif race_choice == "Robots" or race_choice == "robots" or race_choice == "bots" or race_choice == "Bots":
                self.player_race = "Robots"
                return self.player_race

    def assemble_army(self, race_choice):
        if race_choice == "robots" or race_choice == "Robots" or race_choice == "ROBOTS":
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
                print(units.name, "wielding a", units.weapon)
            self.fleet = players_army
            return players_army

        elif race_choice == "dinosaurs" or race_choice == "Dinosaurs" or race_choice == "dinos" or race_choice == "Dinos":
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
            print("You must roll to/over your success to succeed a hit")
            while dino1.health > 1 or dino2.health > 1 or dino3.health > 1 or robo1.health > 1 or robo2.health > 1 or robo3.health > 1:
                print(" ")
                print("______________________Round:", rounds, "___FIGHT!!_______________________________________")
                print("a: attack", dino1.type, " HP:", dino1.health, "     |", "(a) name:", robo1.name, " HP:", robo1.health, " PL:", robo1.power_level)
                print("b: attack", dino2.type, " HP:", dino2.health, "      |", "(b) name:", robo2.name, " HP:", robo2.health, " PL:", robo1.power_level)
                print("c: attack", dino3.type, " HP:", dino3.health, "     |", "(c) name:", robo3.name, " HP:", robo3.health, " PL:", robo3.power_level)
                print("f: Flee:                                                                                      ")
                print("________^ THE ENEMY DINOSAURS ^_____________________^ YOUR ROBOTS ^_____________________")
                print(" ")
                while dino1.health > 0 or dino2.health > 0 or dino3.health > 0:
                    if robo1.health < 1 and robo2.health < 1 and robo3.health < 1:
                        print(" ")
                        print("The Dinosaurs destroy your machines, and having no more resources for battle..")
                        print("The Commander turns the ship away from earth, and sets off to another planet to make home.")
                        print("One with far less ferocious beasts... today on earth, no one is aware of this past encounter.")
                        print(
                            "Perhaps if your race wasn't only 1/2 foot tall, your 10ft gundam-style robots could have stood a chance.")
                        print("YOU LOSE~")
                        return True
                    elif robo1.health > 0 or robo2.health > 0 or robo3.health > 0:
                        break
                while robo1.health > 0 or robo2.health > 0 or robo3.health > 0:
                    if dino1.health < 1 and dino2.health < 1 and dino3.health < 1:
                        print(" ")
                        print("OUTSTANDING!! YOU WIN!! Despite the great disadvantage of size, your race overcame...")
                        print(
                            "and although you won the battle, your entire race was later overcome by hordes of more dinos.")
                        print(
                            "The few left of your race fled the planet, never to return, instead looking for a new home.")
                        print(
                            "Though, you did basically cause the extinction of the dinosaurs, you fled without realizing it.")
                        print(
                            "Thus, that is what really happen to the dinosaurs, and why aliens haven't been contacted since.")
                        return True
                    elif dino1.health > 0 or dino2.health > 0 or dino3.health > 0:
                        break
                enemy = input("Which dinosaur do you want to attack?:")
                while enemy != "a" or enemy != "b" or enemy != "c" or enemy != "f":
                    if enemy == "f":
                        area = BotBattlefield()
                        return [False, area.area2b]
                    if enemy == "a" or enemy == "b" or enemy == "c":
                        break
                    else:
                        enemy = input("Which dinosaur do you want to attack?")
                fighter = input("Which robot do you want to attack with??:")
                while fighter != "a" or fighter != "b" or fighter != "c":
                    if fighter == "a" or fighter == "b" or fighter == "c":
                        break
                    else:
                        fighter = input("Which robot do you want to attack with?")
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
        if who.type == "X___DEAD___" or whom.name == "X___DEAD___":
            print("Sorry, but the dead cannot fight")
        else:

            if self.fleet.fleet[0].name == "_Repair_Bot" or self.fleet.fleet[1].name == "_Repair_Bot" or self.fleet.fleet[2].name == "_Repair_Bot" and self.fleet.fleet[0].weapon == "monkey wrench" or self.fleet.fleet[1].weapon == "monkey wrench" or self.fleet.fleet[2].weapon == "monkey wrench":
                if self.fleet.fleet[0].name != "X___DEAD___":
                    self.fleet.fleet[0].health += 1.5
                    print("_Repair_Bot repairs, ", self.fleet.fleet[0].name)
                if self.fleet.fleet[1].name != "X___DEAD___":
                    self.fleet.fleet[1].health += 1.5
                    print("_Repair_Bot repairs: ", self.fleet.fleet[1].name)
                if self.fleet.fleet[2].name != "X___DEAD___":
                    self.fleet.fleet[2].health += 1.5
                    print("_Repair_Bot repairs: ", self.fleet.fleet[2].name)
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
            print(who.type, "retaliates against you in self-defense!", "You receive,", who.attack_power, "damage!")
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
            who.type = "X___DEAD___"
        if whom.health < 1:
            whom.name = "X___DEAD___"

    def battle_start_for_dinosaurs(self, rounds, players_army, enemies_army):
            print("Time to ENGAGE")
            dino1 = players_army.herd[0]
            dino2 = players_army.herd[1]
            dino3 = players_army.herd[2]
            robo1 = enemies_army.fleet[0]
            robo2 = enemies_army.fleet[1]
            robo3 = enemies_army.fleet[2]
            print("You must roll to/over your success to succeed a hit")
            print(" ")
            while robo1.health > 1 or robo2.health > 1 or robo3.health > 1 and dino1.health > 1 or dino2.health > 1 or dino3.health > 1:
                if dino1.health < 1 and dino2.health < 1 and dino3.health < 1:
                    print(" ")
                    print("The Dinosaurs destroy your machines, and having no mor resources for battle..")
                    print("The Commander turns the ship away from earth, and sets off to another planet to make home.")
                    print("One with far less ferocious beasts...")
                    print("Perhaps if your race wasn't only 1/2 foot tall, your 10ft gundam-style robots could have stood a chance.")
                    print("YOU LOSE~")
                    return True
                if robo1.health < 1 and robo2.health < 1 and robo3.health < 1:
                    print("YOU WIN! ")
                    print("Using your superior technology and intelligence, you destroyed the dinosaurs from off the face of the planet.")
                    print("Sadly, later... a homosapien came to visit your race on earth with greetings, and infected you all")
                    print("with a infections disease, that although they themselves were immune to, wiped out your entire race.")
                    print("Thus, this is how the dinosaurs went extinct, and aliens haven't contacted humans since.....")
                    return True
                print("____________________________Round:", rounds, "___FIGHT!!___________________________________")
                print("a: attack with: ", dino1.type, " HP:", dino1.health, "  |", "a: attack ", robo1.name, " HP: ", robo1.health)
                print("b: attack with: ", dino2.type, " HP:", dino2.health, "  |",  "b: attack ", robo2.name, "   HP: ", robo2.health)
                print("c: attack with: ", dino3.type, " HP:", dino3.health, "  |", "c: attack ", robo3.name, "HP: ", robo3.health)
                print("__________^ YOUR DINOSAURS ^___________________^_THE ENEMY ROBOTS_^________________")
                print(" ")
                enemy = input("Who do you to attack with?:")
                while enemy != "a" or enemy != "b" or enemy != "c":
                    if enemy == "a" or enemy == "b" or enemy == "c":
                        break
                    else:
                        enemy = input("Which dinosaur do you want to attack with?")
                fighter = input("Whom do you want to attack??:")
                while fighter != "a" or fighter != "b" or fighter != "c":
                    if fighter == "a" or fighter == "b" or fighter == "c":
                        break
                    else:
                        fighter = input("Which robot do you want to attack?")

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
        if who.type == "X___DEAD___" or whom.name == "X___DEAD___":
            print("Sorry, but the dead cannot fight")
        else:
            if whom.name == "_Repair_Bot" and who.health < 100:
                whom.health += 10
                print(whom.name, "repairs himself regaining +10 health")
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
                if whom.type == "___T-Rex___":
                    print(whom.type, "attacks", who.name, "with", whom.type, "and crushes,", who.name, "with his jaws!")
                    print("dealing", whom.attack_power, "damage to", who.name)
                    who.health -= whom.attack_power
                    whom.energy - 10
                if whom.type == "Triceratops":
                    tri_rannum = random.randint(0, 7)
                    if tri_rannum > 3:
                        print(whom.type, "charges in and gouges", who.name, "with a", whom.attack1, "CRITICAL HIT! 10x3 damage!")
                        print(who.name, "loses", (whom.attack_power * 2), "health.")
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
                        if ptero_rannum > 3:
                            e_rannum = random.randint(0, 7)
                            print("Your attempt [roll: ", ptero_rannum, "success: 4] was a success!")
                            print("his new roll is:  [roll:", e_rannum, "success 3]")
                            if e_rannum > 2:
                                print("However, he regains his vision quickly and is still able to attack")
                                print("Your attack still dealt", (whom.attack_power -15), "damage")
                                who.health -= (whom.attack_power -15)
                                whom.energy -= 10
                            else:
                                print("He will definitely miss his next attack")
                                print(' ')
                                print("*CRITICAL STRIKE* your attack dealt", (whom.attack_power +5), "damage")
                                who.health -= (whom.attack_power +5)
                                whom.energy -= 10
                        else:
                            print("Your attempt: [roll : ", ptero_rannum,"success: 4] You failed to cause the enemy to re-roll.")
                            print("Your attack still dealt", (whom.attack_power - 15), "damage.")
                            who.health -= (whom.attack_power - 15)
                            whom.energy -= 10
                    else:
                        print("Your attack deals", (whom.attack_power -15), "damage.")
                        who.health -= (whom.attack_power -15)
                        whom.energy -= 10
            if attack_choice == "b" or attack_choice == "B":
                if whom.type == "___T-Rex___":
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
        elif p_rannum < 3 and whom.energy > 0:
            print(" ")
            print("You stumble before you can even decide on what move to use...")
            print("**    **    **    ** Stumble**    ** Stumble **    **    **    *")
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
            who.name = "X___DEAD___"
        if whom.health < 1:
            whom.type = "X___DEAD___"

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

        elif race_choice == "dinosaurs" or race_choice == "DINOSAURS" or race_choice == "dinos" or race_choice == "Dinosaurs" or race_choice == "Dinos":
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
                print(units.name, "wielding a", units.weapon)
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
        self.area2b = "You are just past the center of the valley, dinosaurs near to the east..."
        self.area3 = "You are in enemy territory, enemies in sight!"
        self.area_end = "END"

    def begin_journey(self, area, players_army):
        print(" ")
        print("          Directions ( E )")
        print(" ")
        print(self.area1)
        if area == self.area1:
            print("type look and check your surroundings, or continue east by typing e ")
            action1 = input(" ")
            while action1 != "l" or action1 == "look" or action1 == "e":
                if action1 == "l" or action1 == "look" or action1 == "e":
                    break
                else:
                    action1 = input("Sorry, I didn't recognize that command.  Directions:  (       E )")
            if action1 == "look" or action1 == "l":
                print("There's a giant bone barely sticking out of a pool of tar here...")
                take_club = input("It might make for a very heavy hitting club... take? y or n ")
                while take_club != "y" or take_club != "n":
                    if take_club == "y":
                        break
                    if take_club == "n":
                        break
                    else:
                        take_club = input("Sorry, please type either y or n ")
                if take_club == "y":
                    weapon = Weapon()
                    weapon.equip_club(players_army)
                    print("Nothing much else in this area, directions available? e ")
                    action2 = input("")
                    if action2 == "e" or action2 == "E":
                        return self.area2
                    while action2 != "e" or action2 != "E":
                        if action2 == "e" or action2 == "E":
                            return self.area2
                        else:
                            action2 = input("There's not much else here, might as well go east. (e) ")
                if take_club == "n":
                    print("the giant bone begins to sink into the tar, then disappears.")
                    action3 = input("Nothing much else in the area, directions available? e ")
                    if action3 == "e" or action3 == "E":
                        return self.area2
                    while action3 != "e" or action3 != "e":
                        if action3 == "e" or action3 == "E":
                            return self.area2
                        else:
                            action3 = input("There's not much else here, might as well go east. (e) ")

            if action1 == "e" or action1 == "E":
                print("You continue eastward.")
                return self.area2
            else:
                direction = input("Directions: e ")
                if direction == "e" or direction == "E":
                    return self.area2a
                while direction != "e" or direction != "E":
                    if direction == "e" or direction != "E":
                        return self.area2a
                    else:
                        direction = input("There's nothing much here, you might as well go east..")

        if area == self.area1a:
            direction = input("Directions: e ")
            if direction == "e" or direction == "E":
                return self.area2a
            while direction != "e" or direction != "E":
                if direction == "e" or direction == "E":
                    return self.area2a
                else:
                    direction = input("There's nothing here, you might as well go east..")

    def begin_journey2(self, area, players_army):
        print(" ")
        print("                Directions (W and E)                 ")
        print(" ")
        print(self.area2)
        if self.area2b == area:
            for units in players_army.fleet:
                if units.name == "_Repair_Bot":
                    print("You can repair your robot party for +30 health and +100 power_level for the cost of -100 from", units.name, "power_level.")
                    print("Or, you can use -20 of _Repair_Bot's power_level and the cost of one of your party members lives..")
                    print("And using parts from your sacrificed robot of choice, _Repair_Bot can give the remainder of that sacrificed Bot's")
                    print("attack power, energy and +50 HP to any surviving bot of your choice.")
                    fled = input("(a) Sacrifice a bot? Or (b) Heal the party at the cost of _Repair_Bot's energy? or (c) return to battle. ")
                    while fled != "a" or fled != "b" or fled != "c":
                        if fled == "a" or fled == "b" or fled == "c":
                            break
                        else:
                            fled = input("Please use a, b, or c for your answer.")
                    if fled == "a" or fled == "A":
                        for robos in players_army.fleet:
                            if robos.name == "_Repair_Bot":
                                robos.power_level -= 20
                        for unit in players_army.fleet:
                            if unit.health > 0 and unit.name != "_Repair_Bot":
                                print(" ")
                                print(unit.name)
                                sacrifice = input("Would you like to sacrifice this bot? y or n")
                                if sacrifice == "y" or sacrifice == "Y":
                                    unit.name = "X___DEAD___"
                                    unit.health -= 200
                                    sacrificer_ap = unit.attack_power
                                    sacrificer_pl = unit.power_level
                                    break
                                if sacrifice == "n" or sacrifice == "N":
                                    continue
                                while sacrifice != "y" or sacrifice != "n":
                                    if sacrifice == "y":
                                        unit.name = "X___DEAD___"
                                        unit.health -= 200
                                        sacrificer_ap = unit.attack_power
                                        sacrificer_pl = unit.power_level
                                        break
                                    if sacrifice == "n":
                                        continue
                                    else:
                                        sacrifice = input("Would you like to sacrifice this bot? y or n")
                        print("Which bot do you want to re-build to give more power?")
                        for left_overs in players_army.fleet:
                            if left_overs.name != "X___DEAD___":
                                print(" ")
                                print(left_overs.name)
                                re_build = input("Would you like to rebuild this bot? y or n")
                                if re_build == "y" or re_build == "Y":
                                    left_overs.attack_power += sacrificer_ap
                                    left_overs.power_level += sacrificer_pl
                                    left_overs.health += 50
                                    print(left_overs.name, "now has..", left_overs.health, "HP", left_overs.attack_power, "Attack_Power", unit.power_level, "Power_Level")
                                    return self.area2a
                                if re_build == "n" or re_build == "N":
                                    print("If you run out of options, you will just have to continue back to battle.")
                                    continue
                                while re_build != "y" or re_build != "Y" or re_build != "N" or re_build != "n":
                                    if re_build == "y" or re_build == "Y":
                                        left_overs.attack_power += sacrificer_ap
                                        left_overs.power_level += sacrificer_pl
                                        left_overs.health += 50
                                        print(left_overs.name, "gained,", left_overs.health, "HP", left_overs.attack_power, "Attack_Power", unit.power_level, "Power_Level")
                                        return self.area2a
                                    if re_build == "n" or re_build == "N":
                                        print("if you run out of options, you will just have to continue back to battle.")
                                        continue
                                    else:
                                        re_build = input("Would you like to rebuild this bot? y or n")
                    if fled == "b" or fled == "B":
                        for members in players_army.fleet:
                            if members.name == "_Repair_Bot":
                                if members.power_level < 100:
                                    print("Sorry, but,", members.name, "doesn't have enough power_level for this... PL: ", members.power_level)
                                    return self.area2a
                                else:
                                    members.power_level -= 200
                        for robots in players_army.fleet:
                            robots.health += 30
                            robots.power_level += 100
                        return self.area2a
                    if fled == "c" or fled == "C":
                        return self.area2a

        elif area == self.area2:
            action3 = input("You see the way you came back to the west, and to the east Dinosaurs in the short distance... ")
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
                        print(" ")
                        print("         Directions (W   and   E)")
                        move = input("Well, nothing else here, might as well go east toward the battle..")
                        if move == "e" or move == "E":
                            return self.area3
                        if move == "w" or move == "W":
                            return self.area1a
                        while move != "e" or move != "E" or move != "w" or move != "W":
                            if move == "e" or move == "E":
                                return self.area3
                            if move == "w" or move == "W":
                                return self.area1a
                            else:
                                move = input("Nothing else here, might as well go east to the battle. (e) ")

                    if bot_choice == "b":
                        robo2.attack_power += 15
                        robo2.power_level += 100
                        robo2.health += 50
                        print(robo2.name, "feels a surge of power!")
                        print("You better get moving! Commander says hurry up!")
                        move = input("Well, nothing else here, might as well go east toward the battle.. (e)")
                        if move == "e" or move == "E":
                            return self.area3
                        if move == "w" or move == "W":
                            return self.area1a
                        while move != "e" or move != "E" or move != "w" or move != "W":
                            if move == "e" or move == "E":
                                return self.area3
                            if move == "w" or move == "W":
                                return self.area1a
                            else:
                                move = input("Nothing else here, might as well go east to the battle. (e) ")

                    if bot_choice == "c":
                        robo3.attack_power += 15
                        robo3.power_level += 100
                        robo3.health += 50
                        print(robo3.name, "feels a surge of power!")
                        print("You better get moving! Commander says hurry up!")
                        move = input("Well, nothing else here, might as well go east toward the battle.. (e)")
                        if move == "e" or move == "E":
                            return self.area3
                        if move == "w" or move == "W":
                            return self.area1a
                        while move != "e" or move != "E" or move != "w" or move != "W":
                            if move == "e" or move == "E":
                                return self.area3
                            if move == "w" or move == "W":
                                return self.area1a
                            else:
                                move = input("Nothing else here, might as well go east to the battle. (e) ")
                    else:
                        print("the crystal shatters in your hands! Be more gentle next time... now get a move on")
                        move = input("Well, nothing else here, might as well go east toward the battle.. (e)")
                        if move == "e" or move == "E":
                            return self.area3
                        if move == "w" or move == "W":
                            return self.area1a
                        while move != "e" or move != "E" or move != "w" or move != "W":
                            if move == "e" or move == "E":
                                return self.area3
                            if move == "w" or move == "W":
                                return self.area1a
                            else:
                                move = input("Nothing else here, might as well go east to the battle. (e) ")
                else:
                    print("Oh well, who cares about POWER!!! In a time like this??")
                    print("well, better get a move on...")
                    move1 = input("Well, nothing else here, might as well go east toward the battle.. (e)")
                    if move1 == "e" or move1 == "E":
                        return self.area3
                    if move1 == "w" or move1 == "W":
                        return self.area1a
                    while move1 != "e" or move1 != "E" or move1 != "w" or move1 != "W":
                        move1 = input("Nothing else here, might as well go east to the battle. (e) ")
                        if move1 == "e" or move1 == "E":
                            return self.area3
                        if move1 == "w" or move1 == "W":
                            return self.area3

            if action3 == "w" or action3 == "W" or action3 == "west":
                for units in players_army.fleet:
                    if units.name == "_Tank360_R_" and units.weapon != Weapon().weapon_tank_list[0]:
                        return self.area1
                    elif units.name == "_Tank360_R_" and units.weapon == Weapon().weapon_tank_list[0]:
                        return self.area1a
                return self.area1
            elif action3 == "e" or action3 == "E" or action3 == "east":
                return self.area3
            else:
                move2 = input("Well, nothing else here, might as well go east toward the battle.. (e)")
                if move2 == "e" or move2 == "E":
                    return self.area3
                if move2 == "w" or move2 == "W":
                    return self.area1a
                while move2 != "e" or move2 != "E" or move2 != "w" or move2 != "W":
                    move2 = input("Nothing else here, might as well go east to the battle. (e) ")
                    if move2 == "e" or move2 == "E":
                        return self.area3
                    if move2 == "w" or move2 == "W":
                        return self.area1a

        elif self.area2a == area:
            action4 = input(" ")
            if action4 == "e" or action4 == "E":
                return self.area3
            if action4 == "w" or action4 == "W":
                return self.area1a
            while action4 != "e" or action4 != "E" or action4 != "w" or action4 != "W":
                if action4 == "l" or action4 == "look":
                    print("Nothing out of the ordinary here...")
                if action4 == "e" or action4 == "E":
                    return self.area3
                if action4 == "w" or action4 == "W":
                    return self.area1a
                else:
                    action4 = input(" Directions (W  and  E)     ")

    def begin_journey3(self, area, player_army):
        print(area)
        print("You come into contact with hostile, ravage, giant DINOSAURS!!!")
        print(" ")
        return "battle"


class DinoBattlefield:
    def __init__(self):
        self.area1 = "You stand at the far east of the valley, enjoying leisurely time"

    def begin_dino_journey(self, area):
        print(area)
        print("The ___T-Rex___ munches on some small sheep, the Triceratops seems unafraid, with the Pterodactyl flying high in the sky.")
        print("All the sudden, robots from the west come toward you and begin to battle!")
        return "battle"

class Weapon:
    def __init__(self):
        self.weapon = ""
        self.weapon_list = ["laser", "dino_blaster03", "gatling gun"]
        self.weapon_tank_list = ["giant bone maul", "sword and shield", "greatsword"]
        self.weapon_repair_list = ["monkey wrench", "hammer"]

    def equip_club(self, players_army):
        for units in players_army.fleet:
            if units.name == "_Tank360_R_" and units.weapon != "giant bone maul":
                print("Only _Tank360_R_ is interested in using this...")
                equip_choice = input("Would you like to equip him with it, instead of his current weapon? y or n ")
                if equip_choice == "y":
                    weapon = Weapon().weapon_tank_list[0]
                    units.weapon = weapon
                    units.attack_power += 5
                    print("You equip the", units.weapon, "with _Tank360_R_. His attack power is now:",
                          units.attack_power, "+5")
                    break
                if equip_choice == "n":
                    break
                while equip_choice != "y" or equip_choice != "n":
                    if equip_choice == "y":
                        units.weapon = "giant bone maul"
                        units.attack_power += 5
                        weapon = Weapon().weapon_tank_list[0]
                        self.weapon = weapon
                        print(" ")
                        print("You equip the", weapon, " with _Tank360_R_. His attack power is now:",
                              units.attack_power, "+5")
                        break
                    if equip_choice == "n":
                        break
                    else:
                        equip_choice = input("Press y if you want to equip or if not then press n")

        print("There's nothing special here...")

