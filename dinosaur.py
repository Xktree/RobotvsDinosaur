# Instantiation of class dinosaur

class Dinosaur:
    def __init__(self, name, attack_power, hp):
        self.name = name
        self.attack_power = attack_power
        self.hp = "100"

    def assault_robot(self, robot):
        robot.hp -= self.attack_power
        print(f"{self.name} assaults {robot.name} and deals {self.attack_power} damage. {robot.name} has {robot.health} hp remaining.")