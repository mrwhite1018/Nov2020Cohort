#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Character():
    def __init__(self, health, power, bounty):
        self.health = health
        self.power = power
        self.bounty = bounty

    def alive(self):

        if self.health > 0:
            return True
        else:
            return False


class Hero(Character):
    def __init__(self, health, power, bounty):
        self.character_name = "hero"
        super(Hero, self).__init__(health, power, bounty)	

class 

class Goblin(Character):
    def __init__(self, health, power, bounty):
        self.character_name = "goblin"
        super(Goblin, self).__init__(health, power, bounty)

class Zombie(Character):
    def __init__(self, health, power, bounty):
        self.character_name = "zombie"
        super(Zombie, self).__init__(health, power, bounty)

class Wizard(Character):
    def __init__(self, health, power, bounty):
        self.character_name = "wizard"
        super(Wizard, self).__init__(health, power, bounty)

class Medic(Character):
    def __init__(self, health, power, bounty):
        self.character_name = "medic"
        super(Medic, self).__init__(health, power, bounty)

class Shadow(Character):
    def __init__(self, health, power, bounty):
        self.character_name = "shadow"
        super(Shadow, self).__init__(health, power, bounty)

class Dragon(Character):
    def __init__(self, health, power, bounty):
        self.character_name = "dragon"
        super(Dragon, self).__init__(health, power, bounty)





    def attack(self, enemy):        

        # Hero attacks goblin
        if(enemy.character_name != "zombie"):
            enemy.health -= self.power
        elif(enemy.character_name == "goblin"):
            enemy.health -= self.power

        if(self.character_name == "hero"):
            print(f"You do {self.power} damage to the {enemy.character_name}.")
        elif(self.character_name == "goblin" or self.character_name == "zombie"):
            print(f"The {self.character_name} does {self.power} damage to you.")
        elif(self.character_name == "wizard" or self.character_name == "wizard"):
            print(f"The {self.character_name} does {self.power} damage to you.")
        # Goblin attacks hero

    def print_status(self):
        if self.character_name == "hero":
            print(f"You have {self.health} health and {self.power} power.")
        elif self.character_name == "goblin" or self.character_name == "zombie":
            print(f"The {self.character_name} has {self.health} health and {self.power} power.")
        elif self.character_name == "wizard" or {self.character_name == "wizard":
            print(f"The {self.character_name} has {self.health} health and {self.power} power.")

    def main():

    hero = Hero(10, 5, 7)
    goblin = Goblin(6, 2, 8)
    zombie = Zombie(10, 1, 0)
    shadow = Shadow(1, 4, 5)
    medic = Medic(4, 2, 5)
    dragon = Dragon(12, 6, 11)
    wizard = Wizard(5, 5, 8)

    
    
    

while enemy.alive() and hero.alive():

        hero.print_status()
        enemy.print_status()
        print()
        print("What do you want to do?")
        print(f"1. fight {enemy.character_name}")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks enemy
            hero.attack(enemy)
            

            if not enemy.alive():
                print(f"The {enemy.character_name} is dead.")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if enemy.alive():
            # enemy attacks hero
            enemy.attack(hero)

            if not hero.alive():
                print("You are dead.")

main()