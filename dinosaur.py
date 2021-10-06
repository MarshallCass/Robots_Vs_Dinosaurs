class Dinosaur:
    def _init_(self, name, hit_points, attack_type):
        self.name = name
        self.hit_points = hit_points
        self.attack_type = attack_type

    def dinosaur_attack(self, robot):
        robot.robot_hit_points -= self.dinosaur_attack
        
        