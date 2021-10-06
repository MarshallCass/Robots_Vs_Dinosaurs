from fleet import Robot_Fleet
from herd import Dino_Herd

class Battlefield:
    def _init_(self):
        self.dino_herd = Dino_Herd()
        self.robot_fleet = Robot_Fleet()

    # def battle_start_option(self, battle_begin):
    #     self.start_battle = input('Would you like to start a battle?')
    #     if self.start_battle == 'yes':
    #         print('Let the Battle begin!')
    #         return battle_begin
    #     else:
    #         print('No Battle Today!')

    def battle_begin(self):
        pass