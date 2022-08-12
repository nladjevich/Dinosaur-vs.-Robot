from weapons import Weapon

class Robot:
    def __init__(self, name_input):
        self.name = name_input
        self.health = 100
        self.active_weapon = Weapon("Sword", 30)
        pass

    def attack(self, dinosaur):
        return dinosaur - self.active_weapon.attack_power