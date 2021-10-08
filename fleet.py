from robot import Robot
from weapon import Weapon

class Robot_Fleet:
    def _init_(self):
        self.robot_list = []
        self.weapon_list = []

    def availible_fleet(self):
        robot_one = Robot('Utility', 125, 10)
        robot_two = Robot('Boxie Combat', 150, 20)
        robot_three = Robot('Humanoid', 100, 5)
        self.robot_list.append(robot_one, robot_two, robot_three)
        weapon_one = Weapon('Sledgehammer', 15)
        weapon_two = Weapon('Lazer', 45)
        weapon_three =  Weapon('Slingshot', 5)
        self.weapon_list.append(weapon_one, weapon_two, weapon_three)