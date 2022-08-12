
from arena import Arena
from robot import Robot
from dinosaur import Dinosaur
from weapons import Weapon

current_arena = Arena()

game = current_arena.run_game()
if game == "Yes":
    current_arena.display_welcome()
    current_arena.battle_phase()
    