from fleet import Robot_Fleet
from herd import Dino_Herd
import random

class Battlefield:
    def _init_(self):
        self.dino_herd = Dino_Herd()
        self.robot_fleet = Robot_Fleet()

    def run_game(self):

        self.team_selection = input('To be robots or dinosaurs?')
        if self.team_selection == 'robots':
            team_robots = []
            team_robots.append(random.choices(self.robot_fleet, length=3))
        else:
            pass
  
test = Battlefield()
test.run_game()