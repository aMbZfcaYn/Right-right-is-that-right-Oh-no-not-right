from enum import Enum

class PlayerSettings:
    width = 48
    height = 54
    animationTime = 6

class WindowSettings:
    width = 1000
    height = 800

class GameState(Enum):
    MAIN_MENU = 1
    GAME_PLAY_ORIGIN = 2
    GAME_PLAY_LEVEL = 3
    GAME_PLAY_PAUSE = 4

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