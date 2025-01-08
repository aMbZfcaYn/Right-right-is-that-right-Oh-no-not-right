import pygame

from Player import Player
from GameManager import Gamemanager
from Settings import *

def run():
    # game init
    pygame.init()
    window = pygame.display.set_mode((WindowSettings.width, WindowSettings.height))
    pygame.display.set_caption("Genshin Impact")

    manager = Gamemanager(window)

    player = Player()
    while True:
        manager.tick(30)            # tick setting
        manager.event_queue(player) # process event queue
        keys = pygame.key.get_pressed()
        #print(player.colliSys)
        # render and update
        if manager.state == GameState.MAIN_MENU:
            manager.render()
        elif manager.state == GameState.END_GAME:
            manager.render()
        else:
            player.update(keys, manager.scene)
            manager.update(player)
            manager.render()
            player.draw(window, manager.scene.cameraX, manager.scene.cameraY) 

        pygame.display.flip()



if __name__ == "__main__":
    run()