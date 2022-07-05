# Imports

from robot import Robot 

# Instantiation of class Fleet

class Fleet: 
    def __init__(self):
        self.robots = []
        self.create_fleet()

    def create_fleet(self):
        robot_1 = Robot("C829")
        self.robots.append(robot_1)
        robot_2 = Robot("C269")
        self.robots.append(robot_2)
        robot_3 = Robot("C329")
        self.robots.append(robot_3)
        
