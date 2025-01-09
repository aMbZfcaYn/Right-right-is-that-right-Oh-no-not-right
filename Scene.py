import pygame
import Map
import Player
from Settings import *

class Scene:
    def __init__(self, window, Initial_X, Initial_Y):
        self.state = None
        self.map = None
        self.obstacles = None
        self.background = None

        self.window = window

        self.cameraX = Initial_X
        self.cameraY = Initial_Y

    def check_draw(self, Obj):
        if Obj is not None:
            for sprite in Obj:
                drawRect = sprite.rect.move(-self.cameraX, -self.cameraY)
                self.window.blit( sprite.image, drawRect )

    # render for every scene
    def render(self):
        if self.state == GameState.GAME_PLAY_ORIGIN:
            for i in range(SceneSettings.scene_tileXnum):
                for j in range(SceneSettings.scene_tileYnum):
                    self.window.blit(self.map[i][j], (SceneSettings.tileWidth * i - self.cameraX, SceneSettings.tileHeight * j - self.cameraY))
        
        if self.state == GameState.GAME_PLAY_LEVEL:
            for i in range(SceneSettings.scene_tileXnum):
                for j in range(SceneSettings.scene_tileYnum):
                    self.window.blit(self.map[i][j], (SceneSettings.tileWidth * i - self.cameraX, SceneSettings.tileHeight * j - self.cameraY))

        self.check_draw(self.background)
        self.check_draw(self.obstacles)
    
    def CAMERA_spawn(self, x, y):
        self.cameraX = x
        self.cameraY = y


class MainMenuScene(Scene):
    def __init__(self, window, Initial_X, Initial_Y):
        super().__init__(window, Initial_X, Initial_Y)
        self.state = GameState.MAIN_MENU
        self.bg = pygame.image.load(r".\assets_library\scenes\Example.png")
        self.bg = pygame.transform.scale(self.bg, (WindowSettings.width, WindowSettings.height))

        self.font = pygame.font.Font(None, DialogSettings.textSize)
        self.text = self.font.render("Press ENTER to start", True, (255, 255, 255))
        self.textRect = self.text.get_rect(center=(WindowSettings.width // 2, WindowSettings.height - 50))

        self.timeCounter = 0
    
    def render(self):
        self.window.blit(self.bg, (0, 0))
        self.timeCounter += 1
        '''
        if self.timeCounter >= DialogSettings.flashCD:
            self.window.blit(self.text, self.textRect)
            if self.timeCounter >= DialogSettings.flashCD * 2:
                self.timeCounter = 0
        '''

class OriginScene(Scene):
    def __init__(self, window, Initial_X, Initial_Y):
        super().__init__(window, Initial_X, Initial_Y)
        self.state = GameState.GAME_PLAY_ORIGIN
        self.map = Map.scene_map()
        self.obstacles = Map.scene_obstacles()

class LevelScene(Scene):
    def __init__(self, window, Initial_X, Initial_Y):
        super().__init__(window, Initial_X, Initial_Y)
        self.state = GameState.GAME_PLAY_LEVEL
        self.map = Map.scene_map()
        self.obstacles = Map.level_obstacles()

class EndGameScene(Scene):
    def __init__(self, window, Initial_X, Initial_Y):
        super().__init__(window, Initial_X, Initial_Y)
        self.state = GameState.MAIN_MENU
        self.bg = pygame.image.load(r".\assets_library\scenes\Example.png")
        self.bg = pygame.transform.scale(self.bg, (WindowSettings.width, WindowSettings.height))

    def render(self):
        self.window.blit(self.bg, (0, 0))