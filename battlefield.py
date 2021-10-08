from fleet import Robot_Fleet
from herd import Dino_Herd
import random

class Battlefield:
    def _init_(self):
        self.herd = Dino_Herd().dinosaur
        self.fleet = Robot_Fleet().robot_list
        self.killed_dinosaurs = []
        self.killed_robots = []

    def run_game(self):

        self.team_selection = input('To be robots or dinosaurs?')
        if self.team_selection == 'robots':
            print(f'Your robot team will begin battle!')
            return self.robots_turn
        else:
            return self.dinosaur_turn

## complete rungame

    def robots_turn(self):
            print(self.robot_list)
            self.robot_attack = input('who would you like to  attack with? robot1 robot2 or robot3 ?')
            print (self.herd)
            self.attack = input('who would you like to  attack with? robot1 robot2 or robot3 ?')
            print (self.herd)
        if self.attack == 1:
            self.robot_attacker = robot_one
            return self.attacker
        elif self.attack == 2:
            self.robot_attacker = robot_two
            return self.attacker
        elif self.attack == 3:
            self.robot_attacker = robot_three
            return self.attacker
            
            target_prompt = input('who would you like to dinosaur attack? 1 2 or 3 ?')
        if target_prompt == 1:
            target = dinosaur_one
            return target
        elif target_prompt == 2:
            target = dinosaur_two
            return target
        elif target_prompt == 3:
            target = dinosaur_three
            return target

        if target.dinosaur_health_points <= 0:
           self.killed_dinosaurs.append(target)
 
    def Dinosour turn(self)
        pass



test = Battlefield()
test.run_game()