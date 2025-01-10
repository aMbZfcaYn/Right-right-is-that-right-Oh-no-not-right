import pygame

from Player import Player
from GameManager import Gamemanager
from Settings import *

def run():
    #init
    pygame.init()
    window = pygame.display.set_mode((WindowSettings.width, WindowSettings.height))
    pygame.display.set_caption("Genshin Impact")
    pygame.display.set_icon( pygame.image.load(r".\assets_library\PlayerBasic\PlayerIdle.png") )
    
    manager = Gamemanager(window)

    player = Player()
    while True:
        print(manager.scene.cameraX, manager.scene.cameraY)
        manager.tick(30)            # tick setting
        manager.event_queue(player) # process event queue
        keys = pygame.key.get_pressed()
        if manager.state == GameState.MAIN_MENU:
            manager.render()
        elif manager.state == GameState.GAME_PLAY_PAUSE:
            manager.render()
        else:
            manager.render()
            player.update(keys, manager.scene)
            manager.update(player)
            player.draw(window, manager.scene.cameraX, manager.scene.cameraY) 

        pygame.display.flip()

if __name__ == "__main__":
    run()