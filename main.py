from arena import Arena
from robot import Robot
from dinosaur import Dinosaur
from weapons import Weapon

Dinosaur1 = Dinosaur("Jerry", 30)
Robot1 = Robot("Metatron")
Weapon1 = ("Sword", 20)


game = Arena.run_game()
if game == "Yes":
    Arena.display_welcome()
    Arena.battle_phase