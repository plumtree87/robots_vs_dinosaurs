class Dinosaurs:
    def __init__(self):
        self.type = ''
        self.health = 100
        self.energy = 100
        self.attack_power = 10

    def set_dino(self):
        print("There are three types of Dinosaurs. Which one would you like?")
        print("(a) Triceratops: +50 health")
        print("(b) T-Rex: +15 attack power -10 health")
        print("(c) Pterodactyl: base stats, but pecks at wires and sensor devices stunning opponents 1 round.")
        choice = input("Which one do you choose?")
        if choice == "a" or "A" or "(a)" or "(B)":
            self.type = "Triceratops"
            self.health += 50
        if choice == "b" or "B" or "(B)" or "(b)":
            self.type = "T-Rex"
            self.health -= 20
            self.attack_power += 15
        if choice == "c" or "C" or "(C)" or "(c)":
            self.type = "Pterodactyl"


class Robots:
    def __init__(self):
        self.name = ''
        self.health = 50
        self.power_level = 100
        self.weapon = ''
        self.attack_power = 10

    def set_bot(self):
        print("There are three types of Robots. Which one would you like?")
        print("(a) Tank360R: +80 health +5 attack power +50 power level.")
        print("(b) DPS99R: -20 health +30 attack power")
        print("(c) RepairBot: base stats, but can heal a party member +35 health per round, if has enough power_level.")
        choice = input("Which one do you choose? Select by pressing the letter of your choice.")
        if choice == "a" or "A" or "(a)" or "(B)":
            self.name = "Tank360R"
            self.health += 80
            self.attack_power += 5
            self.power_level += 50
            self.weapon = "Sword and shield"
        if choice == "b" or "B" or "(B)" or "(b)":
            self.name = "DPS99R"
            self.health -= 20
            self.attack_power += 30
            self.weapon = "Rail-gun"
        if choice == "c" or "C" or "(C)" or "(c)":
            self.name = "RepairBot"
            self.weapon = "monkey wrench"






