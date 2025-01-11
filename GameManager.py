import pygame
import sys

import Scene
import Player
from Settings import *

class Gamemanager():
    def __init__(self, window, player):
        self.window = window
        self.player = player
        self.scene = Scene.MainMenuScene(window, 0, 0)
        self.state = GameState.MAIN_MENU
        self.clock = pygame.time.Clock()

    def tick(self, fps):    # ticks
        self.clock.tick(fps)

    def event_queue(self, player:Player.Player):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                #主菜单的操作
                if event.key == pygame.K_RETURN and self.state == GameState.MAIN_MENU:
                    self.flush_scene(GameState.GAME_PLAY_ORIGIN, player, PosSettings.originX, PosSettings.originY)
                if event.key == pygame.K_ESCAPE and self.state == GameState.MAIN_MENU:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
                #Origin的操作
                if event.key == pygame.K_0 and self.state == GameState.GAME_PLAY_ORIGIN:
                    self.flush_scene(GameState.GAME_PLAY_LEVEL, player, PosSettings.levelX, PosSettings.levelY)
                if event.key == pygame.K_ESCAPE and self.state == GameState.GAME_PLAY_ORIGIN:
                    self.flush_scene(GameState.GAME_PLAY_PAUSE, player, 0, 0)
                #Level的操作
                if event.key == pygame.K_ESCAPE and self.state == GameState.GAME_PLAY_LEVEL:
                    self.flush_scene(GameState.GAME_PLAY_PAUSE, player, 0, 0)
                #Pause的操作
                if event.key == pygame.K_c and self.state == GameState.GAME_PLAY_PAUSE:
                    self.flush_scene(self.scene.preScene, player, self.scene.playerX, self.scene.playerY)
                if event.key == pygame.K_r and self.state == GameState.GAME_PLAY_PAUSE:
                    if self.scene.preScene == GameState.GAME_PLAY_ORIGIN:
                        self.flush_scene(self.scene.preScene, player, PosSettings.originX, PosSettings.originY)
                    elif self.scene.preScene == GameState.GAME_PLAY_LEVEL:
                        self.flush_scene(self.scene.preScene, player, PosSettings.levelX, PosSettings.levelY)
                if event.key == pygame.K_q and self.state == GameState.GAME_PLAY_PAUSE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
                #Dead的操作
                if event.key == pygame.K_r and self.state == GameState.GAME_PLAY_DEAD:
                    player.isDead = False
                    if self.scene.preScene == GameState.GAME_PLAY_ORIGIN:
                        self.flush_scene(self.scene.preScene, player, PosSettings.originX, PosSettings.originY)
                    elif self.scene.preScene == GameState.GAME_PLAY_LEVEL:
                        self.flush_scene(self.scene.preScene, player, PosSettings.levelX, PosSettings.levelY)
                if event.key == pygame.K_q and self.state == GameState.GAME_PLAY_DEAD:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
            
            if event.type == GameEvent.EVENT_PLAYER_DEAD:
                pygame.event.get(GameEvent.EVENT_PLAYER_DEAD)
                self.flush_scene(GameState.GAME_PLAY_DEAD, player, 0, 0)


    def flush_scene(self, GOTO:GameState, player:Player.Player, Initial_X, Initial_Y):  # switch scene
        if GOTO == GameState.GAME_PLAY_PAUSE:
            self.scene = Scene.PauseMenuScene(self.window, Initial_X, Initial_Y, player.rect.left, player.rect.top, self.state)
        elif GOTO == GameState.GAME_PLAY_DEAD:
            self.scene = Scene.DeadMenuScene(self.window, Initial_X, Initial_Y, self.state)
        else:
            if GOTO == GameState.GAME_PLAY_LEVEL:
                self.scene = Scene.LevelScene(self.window, Initial_X, Initial_Y)
            if GOTO == GameState.GAME_PLAY_ORIGIN:
                self.scene = Scene.OriginScene(self.window, Initial_X, Initial_Y)
            player.rect.topleft = ( Initial_X, Initial_Y )
        #player.colliSys = Attributes.Collidable(self.scene)
        self.state = GOTO

    def update_camera(self, player:Player.Player):
        playerCenter = ( player.rect.center )  # 获取玩家当前的位置

        self.scene.cameraX = playerCenter[0] - WindowSettings.width // 2
        self.scene.cameraY = playerCenter[1] - WindowSettings.height // 2

        self.scene.cameraX = max(self.scene.cameraX, 0)
        self.scene.cameraX = min(self.scene.cameraX, SceneSettings.sceneWidth)

        self.scene.cameraY = max(self.scene.cameraY, 0)
        self.scene.cameraY = min(self.scene.cameraY, SceneSettings.sceneHeight)

    def update_machine(self, player):
        for machine in self.scene.machines: machine.update(player)

    def update_coin(self):
        for coin in self.scene.coins: coin.update()

    def update(self, player:Player.Player):
        if self.state != GameState.GAME_PLAY_PAUSE:
            self.update_camera(player)
            self.update_machine(player)
            self.update_coin()

    def render(self):
        
        if self.state == GameState.GAME_PLAY_LEVEL or self.state == GameState.GAME_PLAY_ORIGIN:
            self.scene.render(self.player)
            ui = Scene.GamingUI(self.window, 0, 0, self.player)
            ui.render()
        else:
            self.scene.render()