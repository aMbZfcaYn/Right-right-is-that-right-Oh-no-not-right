import pygame
from enum import Enum

class PlayerSettings:
    width = 48
    height = 54
    animationTime = 6

class NPCSettings:
    width = 60
    height = 60

class WindowSettings:
    width = 1000
    height = 800

class GameState(Enum):
    MAIN_MENU = 1
    GAME_PLAY_ORIGIN = 2
    GAME_PLAY_LEVEL_1 = 3
    GAME_PLAY_LEVEL_2 = 4
    GAME_PLAY_PAUSE = 5
    GAME_PLAY_DEAD = 6

class SceneSettings:
    tileWidth = tileHeight = 40

    scene_tileXnum = 100
    scene_tileYnum = 100
    sceneWidth = scene_tileXnum * tileWidth
    sceneHeight = scene_tileYnum * tileHeight

class DialogSettings:
    boxWidth = 800
    boxHeight = 180
    boxAlpha = 150
    boxStartX = WindowSettings.width // 4           # Coordinate X of the box
    boxStartY = WindowSettings.height // 3 * 2 + 20 # Coordinate Y of the box

    textSize = 48 # Default font size
    textStartX = WindowSettings.width // 4 + 10         # Coordinate X of the first line of dialog
    textStartY = WindowSettings.height // 3 * 2 + 30    # Coordinate Y of the first line of dialog
    textVerticalDist = textSize // 4 * 3                # Vertical distance of two lines

    npcWidth = WindowSettings.width // 5
    npcHeight = WindowSettings.height // 3
    npcCoordX = 0
    npcCoordY = WindowSettings.height * 2 // 3 - 20

    flashCD = 15

class PosSettings:
    originX = 0
    originY = 0

    level_1_X = 400
    level_1_Y = 120

    level_2_X = 80
    level_2_Y = 400

class Images:
    wall = pygame.transform.scale( pygame.image.load(r".\assets_library\tiles\12.jpg"), (40, 40) )
    machine = pygame.transform.scale( pygame.image.load(r".\assets_library\tiles\Machine.jpg"), (40, 40) )
    trap = pygame.transform.scale( pygame.image.load(r".\assets_library\Trap.png"), (40, 25) )
    coin = [pygame.transform.scale( pygame.image.load(rf".\assets_library\Coins\Gold-{i}.png") , (40, 40) ) for i in range(1,5)]
    enemy = [pygame.transform.scale( pygame.image.load(rf".\assets_library\Enemy\Enemy-{i}.png") , (40, 40) ) for i in range(1,5)]

class GameEvent:
    EVENT_PLAYER_DEAD = pygame.USEREVENT + 1


class CoinNum:
    Origin = 2
    Level_1 = 3