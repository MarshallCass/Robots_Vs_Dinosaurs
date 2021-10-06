from robot import Robot
from weapon import Weapon

class Robot_Fleet:
    def _init_(self):
        self.robot = [Robot('Humanoid', 100, 5, Weapon('Slingshot', 5)), Robot('Boxie Combat', 150, 20, Weapon('Lazer', 45)), Robot('Utility', 125, 10, Weapon('Sledgehammer', 15))]
