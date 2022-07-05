# Instantiation of class dinosaur

class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.hp = 100
        self.damage = 50

# Attack robot

    def assault(self, robot):
        if robot.hp >= 0:
            robot.hp = robot.hp - self.attack_power
            print(f"{self.name} assaults {robot.name} and deals {self.attack_power} damage. {robot.name} has {robot.hp} hp remaining.")
            print(f"({robot.name} has {robot.hp} hp left.")
        else: 
            print(f"{robot.name} is already scrapped!")
     