import pygame
import sys

import Scene
import Attributes
import Player
from Settings import *

class Gamemanager():
    def __init__(self, window):
        self.window = window
        self.ui = Scene.GamingUI(window, 0, 0)
        self.scene = Scene.MainMenuScene(window, 0, 0)
        self.state = GameState.MAIN_MENU
        self.clock = pygame.time.Clock()

    def tick(self, fps):    # ticks
        self.clock.tick(fps)

    def get_width(self):
        '''
        if self.state == GameState.GAME_PLAY_CITY:
            return WindowSettings.width * WindowSettings.outdoorScale
        elif self.state == GameState.GAME_PLAY_WILD:
            return SceneSettings.wild_tileXnum * SceneSettings.tileWidth
        else:
            return WindowSettings.width'''
        return WindowSettings.width
    def get_height(self):
        '''
        if self.state == GameState.GAME_PLAY_CITY:
            return WindowSettings.height * WindowSettings.outdoorScale
        elif self.state == GameState.GAME_PLAY_WILD:
            return SceneSettings.wild_tileYnum * SceneSettings.tileHeight
        else:
            return WindowSettings.height'''
        return WindowSettings.height

    def event_queue(self, player:Player.Player):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and self.state == GameState.MAIN_MENU:
                    self.flush_scene(GameState.GAME_PLAY_ORIGIN, player, 0, 0)

                if event.key == pygame.K_0 and self.state == GameState.GAME_PLAY_ORIGIN:
                    self.flush_scene(GameState.GAME_PLAY_LEVEL, player, 400, 120)
                
                if event.key == pygame.K_ESCAPE and self.state == GameState.GAME_PLAY_ORIGIN:
                    self.flush_scene(GameState.GAME_PLAY_PAUSE, player, 0, 0)

                if event.key == pygame.K_ESCAPE and self.state == GameState.GAME_PLAY_LEVEL:
                    self.flush_scene(GameState.GAME_PLAY_PAUSE, player, 0, 0)
                
                if event.key == pygame.K_ESCAPE and self.state == GameState.MAIN_MENU:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))

                if event.key == pygame.K_c and self.state == GameState.GAME_PLAY_PAUSE:
                    self.flush_scene(self.scene.preScene, player, self.scene.playerX, self.scene.playerY)
            
    def flush_scene(self, GOTO:GameState, player:Player.Player, Initial_X, Initial_Y):  # switch scene
        if GOTO == GameState.GAME_PLAY_PAUSE:
            self.scene = Scene.PauseMenuScene(self.window, Initial_X, Initial_Y, player.rect.left, player.rect.top, self.state)
        else:
            if GOTO == GameState.GAME_PLAY_LEVEL:
                self.scene = Scene.LevelScene(self.window, Initial_X, Initial_Y)
            if GOTO == GameState.GAME_PLAY_ORIGIN:
                self.scene = Scene.OriginScene(self.window, Initial_X, Initial_Y)
            player.rect.topleft = ( Initial_X, Initial_Y )
        player.colliSys = Attributes.Collidable(self.scene)
        self.state = GOTO

    def update_camera(self, player:Player.Player):
        playerCenter = ( player.rect.center )  # 获取玩家当前的位置

        self.scene.cameraX = playerCenter[0] - WindowSettings.width // 2
        self.scene.cameraY = playerCenter[1] - WindowSettings.height // 2

        self.scene.cameraX = max(self.scene.cameraX, 0)
        self.scene.cameraX = min(self.scene.cameraX, SceneSettings.sceneWidth)

        self.scene.cameraY = max(self.scene.cameraY, 0)
        self.scene.cameraY = min(self.scene.cameraY, SceneSettings.sceneHeight)

    def update(self, player:Player.Player):
        if self.state != GameState.GAME_PLAY_PAUSE:
            self.update_camera(player)
            for machine in self.scene.machines:
                machine.update()

    def render(self):
        self.scene.render()
        if self.state == GameState.GAME_PLAY_LEVEL or self.state == GameState.GAME_PLAY_ORIGIN:
            self.ui.render()