# Imports from the fleet and herd classes

from fleet import Fleet
from herd import Herd 
import random

# Instantiation of class battlefield 

class Battlefield:
    def __init__(self):
        self.herd = Herd()
        self.fleet = Fleet()

# Run game

    def run_game(self):
        self.display_welcome()
        self.display_winner(self.battle())

# Welcome messages

    def display_welcome(self):
        print("\n")
        print("Welcome General. Yesterday at 2300 hours, a strange portal emerged over the Amazon Rainforest. Initial scans picked up a large lifeform and an unusual displacement of forest growth within the vicinity of the portal shortly after it's appearance.")
        print("\n")
        print("We have dispatched a team to investigate as of 20 minutes ago.")
        print("\n")
        print("Sir, our strike force has encountered the invaders. It seems a confrontation is about to break out.")
        print("\n")

# Battle of dino and robot/while loop win condition
    def battle(self):
        all_dinosaurs_killed = False 
        all_robots_scrapped = False 
        round_count = 1

        # While loop to continue the game so long as there are living combatants on both sides 

        while all_dinosaurs_killed != True and all_robots_scrapped != True:
            self.robot_turn(random.choice(self.fleet.robots))
            all_dinosaurs_killed = self.display_dinosaur_enemies()
            self.dinosaur_turn(random.choice(self.herd.dinosaurs))
            all_robots_scrapped = self.display_robot_enemies()
            print(f"It is now {round_count}.")
            round_count += 1

        # If loop to return victor of the game 

        if all_dinosaurs_killed == True: 
            print("Threats neutralized!")
        if all_robots_scrapped == True: 
            print("Back to the Jurassic!")
            
# Dinosaur combatant
    def dinosaur_turn(self, dinosaur):
        dinosaur.assault(random.choice(self.herd.dinosaurs))
    
# Robot combatant
    def robot_turn(self, robot):
        robot.assault(random.choice(self.herd.dinosaurs))

# Display dinosaur combatants and hp level 

    def display_dinosaur_enemies(self):
        print(f"{self.herd.dinosaurs[0].name} has {self.herd.dinosaurs[0].hp} remaining")
        print(f"{self.herd.dinosaurs[1].name} has {self.herd.dinosaurs[1].hp} remaining")
        print(f"{self.herd.dinosaurs[2].name} has {self.herd.dinosaurs[2].hp} remaining")
        if self.herd.dinosaurs[0].hp <= 0 and self.herd.dinosaurs[1].hp <= 0 and self.herd.dinosaurs[2].hp <= 0:
            return True 
        
# Display robot combatants and hp level 

    def display_robot_enemies(self):
        print(f"{self.fleet.robots[0].name} has {self.fleet.robots[0].hp} remaining")
        print(f"{self.fleet.robots[1].name} has {self.fleet.robots[1].hp} remaining")
        print(f"{self.fleet.robots[2].name} has {self.fleet.robots[2].hp} remaining")
        if self.fleet.robots[0].hp <= 0 and self.fleet.robots[1].hp <= 0 and self.fleet.robots[2].hp <= 0:
            return True 
         
    def display_winner(self, winner):
        print(winner)
    