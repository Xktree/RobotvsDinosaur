# Import weapons

from weapons import Weapons 

# Instantiation of class robot

class Robot:
    def __init__(self, name, attack_power, hp):
        self.name = name
        self.attack_power = attack_power
        self.hp = "100"

# Attack dinosaur 

    def assault_dinosaur(self, dinosaur):
        if dinosaur.hp >= 0:
            dinosaur.hp -= self.attack_power
            print(f"{self.name} assaults {dinosaur.name} and deals {self.attack_power} damage. {dinosaur.name} has {dinosaur.hp} hp remaining.")
            print(f"({dinosaur.name} has {dinosaur.hp} hp left.")
        else:
            print("{dinosaur.name} is already roadkill!")