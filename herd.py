from dinosaur import Dinosaur

class Dino_Herd:
    def _init_(self):
        self.dinosaur = []

    def dino_herd_availible(self):
        dinosaur_one = Dinosaur('Tyrannosaurus Rex', 300, 50)
        dinosaur_two = Dinosaur('Stegosaurus', 250, 25)
        dinosaur_three = Dinosaur('Pterodactyl', 125, 15)
        self.dinosaur.append(dinosaur_one, dinosaur_two, dinosaur_three)