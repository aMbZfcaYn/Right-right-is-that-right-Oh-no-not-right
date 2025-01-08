import pygame
from Settings import *
from random import randint

# generating maps in every scene
class Block(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = pygame.transform.scale(image, (SceneSettings.tileWidth, SceneSettings.tileHeight))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.lastCameraX = 0
        self.lastCameraY = 0

    def update(self, cameraX, cameraY):
        self.rect.x -= (cameraX - self.lastCameraX)
        self.rect.y -= (cameraY - self.lastCameraY)
        self.lastCameraX = cameraX
        self.lastCameraY = cameraY

def scene_map():
    images = [ pygame.transform.scale( pygame.image.load(rf".\assets_library\tiles\{type}.jpg"), (40, 40), ) for type in range(1,7) ]
    images = [pygame.transform.scale(image, (SceneSettings.tileWidth, SceneSettings.tileHeight)) for image in images]

    mapObj = []
    for i in range(SceneSettings.scene_tileXnum):
        tmp = []
        for j in range(SceneSettings.scene_tileYnum):
            tmp.append(images[randint(0, len(images) - 1)])
        mapObj.append(tmp)

    return mapObj

def scene_obstacles():
    image_wall = pygame.transform.scale( pygame.image.load(r".\assets_library\tiles\12.jpg"), (40, 40) )
    obstacles = []

    for i in range(2 * WindowSettings.width // 40 + 1):
        obstacles.append(Block(image_wall, SceneSettings.tileWidth * i, 760))
    
    for i in range(WindowSettings.width // 40 + 1, 2 * WindowSettings.width // 40 + 1):
        obstacles.append(Block(image_wall, SceneSettings.tileWidth * i, 640))
    return obstacles
    '''
    for i in range(self.map_range[1] // 40 + 1, 2 * self.map_range[1] // 40 + 1):
        self.floors.append(Floor(pygame.Rect(i*40, 640, 40, 40)))

    for i in range(self.map_range[1] // 40 + 1):
        self.floors.append(Floor(pygame.Rect(0, i*40, 40, 40)))'''