import pygame
import Map
import Player
from Settings import *

class Scene:
    def __init__(self, window, Initial_X, Initial_Y):
        self.state = None
        self.map = None
        self.walls = []
        self.machines = []
        self.obstacles = []
        self.traps = []
        self.coins = []
        self.enemies = []
        self.background = None

        self.window = window

        self.cameraX = Initial_X
        self.cameraY = Initial_Y

    def Check_Draw(self, Obj):
        if Obj is not None:
            for sprite in Obj:
                drawRect = sprite.rect.move(-self.cameraX, -self.cameraY)
                self.window.blit( sprite.image, drawRect )

    #获取过的金币不能再次获取， 单独写一个函数
    def Draw_Coin(self, player):
        for i in range( len( self.coins ) ):
            if not player.coinsGet[self.name][i]:
                drawRect = self.coins[i].rect.move(-self.cameraX, -self.cameraY)
                self.window.blit( self.coins[i].image, drawRect )


    # render for every scene
    def render(self, player):
        if self.state == GameState.GAME_PLAY_ORIGIN:
            for i in range(SceneSettings.scene_tileXnum):
                for j in range(SceneSettings.scene_tileYnum):
                    self.window.blit(self.map[i][j], (SceneSettings.tileWidth * i - self.cameraX, SceneSettings.tileHeight * j - self.cameraY))
        
        if self.state == GameState.GAME_PLAY_LEVEL_1:
            for i in range(SceneSettings.scene_tileXnum):
                for j in range(SceneSettings.scene_tileYnum):
                    self.window.blit(self.map[i][j], (SceneSettings.tileWidth * i - self.cameraX, SceneSettings.tileHeight * j - self.cameraY))
        
        if self.state == GameState.GAME_PLAY_LEVEL_2:
            for i in range(SceneSettings.scene_tileXnum):
                for j in range(SceneSettings.scene_tileYnum):
                    self.window.blit(self.map[i][j], (SceneSettings.tileWidth * i - self.cameraX, SceneSettings.tileHeight * j - self.cameraY))

        self.Check_Draw(self.background)
        self.Check_Draw(self.obstacles)
        self.Check_Draw(self.machines)
        self.Check_Draw(self.traps)
        self.Check_Draw(self.enemies)
        self.Draw_Coin(player)
    
    def CAMERA_spawn(self, x, y):
        self.cameraX = x
        self.cameraY = y

class MainMenuScene(Scene):
    def __init__(self, window, Initial_X, Initial_Y):
        super().__init__(window, Initial_X, Initial_Y)
        self.state = GameState.MAIN_MENU
        self.bg = pygame.image.load('assets_library\scenes\WelcomeBg.gif').convert_alpha()
        self.bg = pygame.transform.scale(self.bg, (WindowSettings.width, WindowSettings.height))
        #这是Welcome的文字
        self.Welcome_font = pygame.font.Font(None, 150)
        self.Welcome_surf = self.Welcome_font.render('Welcome!', False, 'Black').convert_alpha()
        self.Welcome_rect = self.Welcome_surf.get_rect(center = (500, 300))
        #这是Press Here To Start的文字
        self.PressHere_font = pygame.font.Font(None, 100)
        self.PressHere_surf = self.PressHere_font.render('Press Enter To Start! :)', False, 'Black').convert_alpha()
        self.PressHere_rect = self.PressHere_surf.get_rect(center = (500, 600))
        #这是Press Here To Start下面的图案
        self.bgPress_suef = pygame.image.load('assets_library\objects\\bg_for_PressHere.png').convert_alpha()
        self.bgPress_suef= pygame.transform.scale(self.bgPress_suef, (880, 200))
        self.bgPress_rect = self.bgPress_suef.get_rect(center = (500, 600))

    def render(self):
        self.window.blit(self.bg, (0, 0))
        self.window.blit(self.Welcome_surf, self.Welcome_rect)
        self.window.blit(self.bgPress_suef, self.bgPress_rect)
        self.window.blit(self.PressHere_surf, self.PressHere_rect)

class PauseMenuScene(Scene):
    def __init__(self, window, Initial_X, Initial_Y, playerX, playerY, preScene):
        super().__init__(window, Initial_X, Initial_Y)
        self.state = GameState.GAME_PLAY_PAUSE
        
        self.playerX = playerX
        self.playerY = playerY
        self.preScene = preScene

        self.test_color = 'Pink'   #字体颜色统一，我先搞成粉色
        #这是Pause文字
        self.Pause_font = pygame.font.Font(None, 100)
        self.Pause_surf = self.Pause_font.render('PAUSE', False, self.test_color).convert_alpha()
        self.Pause_rect = self.Pause_surf.get_rect(center = (500, 150))

        #这是Continue图像和文字
        self.continue_surf = pygame.image.load('assets_library\特殊符号\continue.png').convert_alpha()
        self.continue_surf= pygame.transform.scale(self.continue_surf, (150, 150))
        self.continue_rect = self.continue_surf.get_rect(center = (500, 350))

        self.Continue_font = pygame.font.Font(None, 50)
        self.Continue_surf = self.Continue_font.render('Continue [C]', False, self.test_color).convert_alpha()
        self.Continue_rect = self.Continue_surf.get_rect(center = (500, 450))

        #这是Replay的图像和文字
        self.replay_surf = pygame.image.load('assets_library\特殊符号\\replay.png').convert_alpha()
        self.replay_surf = pygame.transform.scale(self.replay_surf, (80, 80))
        self.replay_rect = self.replay_surf.get_rect(center = (200, 575))

        self.Restart_font = pygame.font.Font(None, 50)
        self.Restart_surf = self.Restart_font.render('Restart [R]', False, self.test_color).convert_alpha()
        self.Restart_rect = self.Restart_surf.get_rect(center = (200, 650))

        #这是Question的图像和文字
        self.question_surf = pygame.image.load('assets_library\特殊符号\\question.png').convert_alpha()
        self.question_surf= pygame.transform.scale(self.question_surf, (80, 80))
        self.question_rect = self.replay_surf.get_rect(center = (500, 575))

        self.Question_font = pygame.font.Font(None, 50)
        self.Question_surf = self.Question_font.render('Help [E]', False, self.test_color).convert_alpha()
        self.Question_rect = self.Question_surf.get_rect(center = (500, 650))

        #这是Home的图像和文字
        self.home_surf = pygame.image.load('assets_library\特殊符号\\Home.png').convert_alpha()
        self.home_surf= pygame.transform.scale(self.home_surf, (80, 80))
        self.home_rect = self.replay_surf.get_rect(center = (800, 575))

        self.Home_font = pygame.font.Font(None, 50)
        self.Home_surf = self.Home_font.render('Quit [Q]', False, self.test_color).convert_alpha()
        self.Home_rect = self.Home_surf.get_rect(center = (800, 650))

    def render(self):
        self.window.blit(self.Pause_surf, self.Pause_rect)
        self.window.blit(self.continue_surf, self.continue_rect)
        self.window.blit(self.Continue_surf, self.Continue_rect)
        self.window.blit(self.replay_surf, self.replay_rect)
        self.window.blit(self.Restart_surf, self.Restart_rect)
        self.window.blit(self.question_surf, self.question_rect)
        self.window.blit(self.Question_surf, self.Question_rect)
        self.window.blit(self.home_surf, self.home_rect)
        self.window.blit(self.Home_surf, self.Home_rect)

class DeadMenuScene(Scene):
    def __init__(self, window, Initial_X, Initial_Y, preScene):
        super().__init__(window, Initial_X, Initial_Y)
        self.preScene = preScene

    def render(self):
        self.window.blit(Images.trap, (0, 0))

class OriginScene(Scene):
    def __init__(self, window, Initial_X, Initial_Y):
        super().__init__(window, Initial_X, Initial_Y)
        self.name = "Origin"
        self.state = GameState.GAME_PLAY_ORIGIN
        self.map = Map.scene_map()
        self.walls = Map.scene_walls()
        self.machines = Map.scene_machines()
        self.coins = Map.scene_coins()
        self.enemies = Map.scene_enemies()

        self.obstacles = self.walls + self.machines

class Level_1_Scene(Scene):
    def __init__(self, window, Initial_X, Initial_Y):
        super().__init__(window, Initial_X, Initial_Y)
        self.name = "Level_1"
        self.state = GameState.GAME_PLAY_LEVEL_1
        self.map = Map.scene_map()
        self.walls = Map.level_1_walls()
        self.machines = Map.level_1_machines()
        self.traps = Map.level_1_traps()

        self.obstacles = self.walls + self.machines

class Level_2_Scene(Scene):
    def __init__(self, window, Initial_X, Initial_Y):
        super().__init__(window, Initial_X, Initial_Y)
        self.name = "Level_2"
        self.state = GameState.GAME_PLAY_LEVEL_2
        self.map = Map.scene_map()
        self.walls = Map.level_2_walls()
        self.machines = Map.level_2_machines()
        self.traps = Map.level_2_traps()
        self.enemies = Map.level_2_enemies()

        self.obstacles = self.walls + self.machines

class GamingUI(Scene):
    def __init__(self, window, Initial_X, Initial_Y, player):
        super().__init__(window, Initial_X, Initial_Y)
        self.test_color = 'Pink'   #字体颜色统一，我先搞成粉色

        #这是Pause图像和文字
        self.pause_surf = pygame.image.load('assets_library\特殊符号\pause.png').convert_alpha()
        self.pause_surf= pygame.transform.scale(self.pause_surf, (40, 40))
        self.pause_rect = self.pause_surf.get_rect(center = (955, 45))

        self.Pause_font = pygame.font.Font(None, 30)
        self.Pause_surf = self.Pause_font.render('pause', False, self.test_color).convert_alpha()
        self.Pause_rect = self.Pause_surf.get_rect(center = (955, 80))

        #这是Heart图像和文字，还有冒号和数字
        self.heart_surf = pygame.image.load('assets_library\coins\Gold-1.png').convert_alpha()
        self.heart_surf= pygame.transform.scale(self.heart_surf, (40, 40))
        self.heart_rect = self.heart_surf.get_rect(center = (45, 45))

        self.Heart_font = pygame.font.Font(None, 30)
        self.Heart_surf = self.Heart_font.render('Coins', False, self.test_color).convert_alpha()
        self.Heart_rect = self.Heart_surf.get_rect(center = (45, 80))

        self.heart_amount_font = pygame.font.Font(None, 50)
        self.heart_amount_surf = self.heart_amount_font.render(f": {player.coins}", False, self.test_color).convert_alpha()
        self.heart_amount_rect = self.heart_amount_surf.get_rect(center = (90, 45))
    
    def render(self):
        self.window.blit(self.pause_surf, self.pause_rect)
        self.window.blit(self.Pause_surf, self.Pause_rect)
        self.window.blit(self.heart_surf, self.heart_rect)
        self.window.blit(self.Heart_surf, self.Heart_rect)
        self.window.blit(self.heart_amount_surf, self.heart_amount_rect)