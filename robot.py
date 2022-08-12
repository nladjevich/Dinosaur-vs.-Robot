from weapons import Weapon

class Robot:
    def __init__(self, name_input):
        self.name = name_input
        self.health = 100
        self.active_weapon = Weapon()
        pass

    def attack(self, dinosaur):
        dinosaur - self.active_weapon.attack_power