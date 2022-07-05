# Import weapons

from weapons import Weapons 

# Instantiation of class robot

class Robot:
    def __init__(self, name):
        self.name = name
        self.weapon = Weapons("Ion Cannon", 50)
        self.hp = 100

# Attack dinosaur 

    def assault(self, dinosaur):
        if dinosaur.hp >= 0:
            dinosaur.hp = dinosaur.hp - self.weapon.attack_power
            print(f"{self.name} assaults {dinosaur.name} and deals {self.weapon.attack_power} damage. {dinosaur.name} has {dinosaur.hp} hp remaining.")
            print(f"({dinosaur.name} has {dinosaur.hp} hp left.")
        else:
            print(f"{dinosaur.name} is already roadkill!")