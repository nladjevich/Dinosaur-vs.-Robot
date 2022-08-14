
from robot import Robot
from dinosaur import Dinosaur

class Arena:
    def __init__(self):
        self.robot = Robot("Metatron")
        self.dinosaur = Dinosaur("Don", 30)
        pass

    def run_game(self):
        game_on = input("Do you want to turn on the game? Yes or No.")
        return game_on

    def display_welcome(self):
        print(f"Welcome to Robot vs. Dinosaur!! {self.dinosaur.name} the Dinosaur vs. {self.robot.name} the Robot!!")

    def battle_phase(self):
        dinosaur_loss = "r_wins"
        robot_loss = "d_wins"
        while self.dinosaur.health or self.robot.health > 0:
            print (f"{self.robot.name} attacks!")
            self.dinosaur.health = self.robot.attack(self.dinosaur.health)
            print(f"{self.dinosaur.name} is at {self.dinosaur.health} health.")
            if self.dinosaur.health <= 0:
                break
            print(f"{self.dinosaur.name} attacks!")
            self.robot.health  = self.dinosaur.attack(self.robot.health)
            print(f"{self.robot.name} is at {self.robot.health} health.")
            if self.robot.health <= 0:
                break
        
    
    def display_winner(self):
        if self.dinosaur.health <= 0:
            print(f"{self.dinosaur.name} the Dinosaur has fallen to {self.robot.name}'s mighty weapon!! Robot Wins!!")
        elif self.robot.health <= 0:
            print(f"{self.robot.name} the Robot has fallen to the fierce claws of {self.dinosaur.name}!! Dinosaur Wins!!")

