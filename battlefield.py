# Imports from the dinosaur, robot, and weapons classes

from dinosaur import Dinosaur
from robot import Robot 
from weapons import Weapons

# Instantiation of class battlefield 

class Battlefield:
    def __init__(self):
        self.dino_health = self.hp


























# Run game

    def run_game(self):
        self.display_welcome()
        self.display_winner(self.battle())
# Welcome messages

    def display_welcome(self):
        print("\n")
        print("Welcome General. Yesterday at 2300 hours, a strange portal emerged over the Amazon Rainforest. Initial scans picked up a large lifeform and an unusual displacement of forest growth within the vicinity of the portal shortly after it's appearance.")
        print("\n")
        print("We have dispatched {robot.name} to investigate as of 20 minutes ago.")
        print("\n")
        print("Sir, {robot.name} has encountered {dinosaur.name}. It seems a confrontation is about to break out.")
        print("\n")

# Battle of dino and robot
    def battle_phase(self):
        dino_slain = False 
        robot_slain = False 
        round_count = 1
        while dino_slain != True and robot_slain != True:
            
# Winner of battle, whoever has the most health after

    def display_winner(self):
        if self.dino_health > 0
    