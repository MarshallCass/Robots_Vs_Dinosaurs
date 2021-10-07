from robot import Robot
from weapon import Weapon

class Robot_Fleet:
    def _init_(self):
        self.robot = []

    def robot_fleet(self):
        robot_one = Robot('Utility', 125, 10, Weapon('Sledgehammer', 15))
        robot_two = Robot('Boxie Combat', 150, 20, Weapon('Lazer', 45))
        robot_three = Robot('Humanoid', 100, 5, Weapon('Slingshot', 5))
        robot_four = Robot('Washamatic', 80, 5, Weapon('Scrub Brush',2))
        self.robot.append(robot_one)
        self.robot.append(robot_two)
        self.robot.append(robot_three)
        self.robot.append(robot_four)