from dinosaur import Dinosaur

class Dino_Herd:
    def _init_(self):
        self.dinosaur = []

    def herd(self):
        dinosaur_one = Dinosaur('Tyrannosaurus Rex', 300, 50)
        dinosaur_two = Dinosaur('Stegosaurus', 250, 25)
        dinosaur_three = Dinosaur('Pterodactyl', 125, 15)
        dinosaur_four = Dinosaur('Titanoboa', 90, 10)
        self.dinosaur.append(dinosaur_one)
        self.dinosaur.append(dinosaur_two)
        self.dinosaur.append(dinosaur_three)
        self.dinosaur.append(dinosaur_four)