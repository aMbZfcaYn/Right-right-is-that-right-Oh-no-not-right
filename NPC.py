import pygame
from Settings import *

from openai import OpenAI
from typing import List, Dict

class NPC(pygame.sprite.Sprite):
    def __init__(self, x = WindowSettings.width // 2, y = WindowSettings.height // 2):
        super().__init__()
        #initialize
        self.image = pygame.transform.scale( pygame.image.load(r".\assets_library\characters\黑暗大骑士.png") , (PlayerSettings.width, PlayerSettings.height) )
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        # states
        self.states = ["Idle", "Move", "Jump", "Fall"]
        self.state = "Idle"
        #collision info
        self.groundCheckDis = 1
        self.isGrounded = False
        self.headCheckDis = 1
        self.headCollide = False
        #move info
        self.moveSpeed = 10
        self.velocity_x = 0
        self.velocity_y = 0
        self.facingRight = True
        self.facingDir = 1
        #jump info
        self.gravity = 3
        self.jumpForce = 35
        
        #animation info
        self.animTimer = 0
        self.animIndex = 0
        self.currentAnim = None
        self.idleAnim = [pygame.transform.scale( pygame.image.load(r".\assets_library\characters\黑暗大骑士.png") , (PlayerSettings.width, PlayerSettings.height) )]
        self.moveAnim = [pygame.transform.scale( pygame.image.load(rf".\assets_library\characters\黑暗大骑士.png") , (PlayerSettings.width, PlayerSettings.height) ) for i in range(1,5)]
        self.jumpAnim = [pygame.transform.scale( pygame.image.load(rf".\assets_library\characters\黑暗大骑士.png") , (PlayerSettings.width, PlayerSettings.height) )]
        self.fallAnim = [pygame.transform.scale( pygame.image.load(rf".\assets_library\characters\黑暗大骑士.png") , (PlayerSettings.width, PlayerSettings.height) )]
    def Awake(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_f]:
            pygame.event.post(pygame.event.Event(GameEvent.EVENT_SHOP))