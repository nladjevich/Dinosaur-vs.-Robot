from robot import Robot

class Dinosaur:
    def __init__(self, name_input, attack_power_input):
        self.name = name_input
        self.attack_power = attack_power_input
        self.health = 100
        pass

    def attack(self, robot):
        return robot - self.attack_power
        



