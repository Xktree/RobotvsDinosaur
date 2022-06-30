# Instantiation of class robot

class Robot:
    def __init__(self, name, attack_power, hp):
        self.name = name
        self.attack_power = attack_power
        self.hp = "100"

    def assault_dinosaur(self, dinosaur):
        dinosaur.hp -= self.attack_power
        print(f"{self.name} assaults {dinosaur.name} and deals {self.attack_power} damage. {dinosaur.name} has {dinosaur.health} hp remaining.")