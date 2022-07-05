# Import Dinosaur 

from dinosaur import Dinosaur 

# Instantiation of class Herd

class Herd: 
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()

    def create_herd(self):
        dino_1 = Dinosaur("Tyrannosaurus Rex", 50)
        self.dinosaurs.append(dino_1)
        dino_2 = Dinosaur("Stegosaurus", 50)
        self.dinosaurs.append(dino_2)
        dino_3 = Dinosaur("Allosaurus", 50)
        self.dinosaurs.append(dino_3)
        
