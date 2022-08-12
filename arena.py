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
        print("Welcome to Robot vs. Dinosaur!!")

    def battle_phase(self):
        remaining_health_dino = self.robot.attack(self.dinosaur.health)
        print(f"Dinosaur is at {remaining_health_dino} health.")
        remaining_health_robot = self.dinosaur.attack(self.robot.health)
        print(f"Robot is at {remaining_health_robot} health.")
    
    def display_winner(self):
        if self.dinosaur.health <= 0:
            print("Robot Wins!!")
        elif self.robot.health <= 0:
            print("Dinosaur Wins!!")

