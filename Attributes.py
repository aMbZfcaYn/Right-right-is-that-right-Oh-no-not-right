import pygame
import Player
import Scene
from Settings import *

# check player collid with every sprites
class Collidable:
    def __init__(self, scene:Scene.Scene):
        self.collidingWith = {
            "obstacle":False,
        }
        self.collidingObject = {
            "obstacle":scene.obstacles
        }
    
    def is_colliding_obstacle(self, player:Player.Player):
        if self.collidingObject["obstacle"] is not None:
            if pygame.sprite.spritecollide(player, self.collidingObject["obstacle"], False):
                self.collidingWith["obstacle"] = True
            else:
                self.collidingWith["obstacle"] = False
        else:
            self.collidingWith["obstacle"] = False

    # check every object that stop player moving
    def is_colliding_not_move(self, player:Player.Player):
        self.is_colliding_obstacle(player)

        return (self.collidingWith["obstacle"])