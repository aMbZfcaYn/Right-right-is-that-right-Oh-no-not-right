import pygame
from Settings import *
from platforme import level
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

    '''def update(self, cameraX, cameraY, player):
        self.rect.x -= (cameraX - self.lastCameraX)
        self.rect.y -= (cameraY - self.lastCameraY)
        self.lastCameraX = cameraX
        self.lastCameraY = cameraY'''

class Machine(Block):
    def __init__(self, image, x, y, dis):
        super().__init__(image, x, y)
        self.tarDis = dis
        self.on = False
        self.returning = False
        self.velocity = 5
        self.moveDis = 0
        self.stayTime = 3
        self.stayTick = 30 * self.stayTime
        
    def update(self):
        if self.moveDis == self.tarDis:
            self.on = False
            self.stayTick -= 1
        if self.stayTick <= 0:
            self.on = False
            self.returning = True
            self.rect = self.rect.move(0, self.velocity * 2)
            self.moveDis -= self.velocity * 2
        if self.moveDis == 0:
            self.stayTick = 30 * self.stayTime
        if self.on:
            self.rect = self.rect.move(0, -self.velocity)
            self.moveDis += self.velocity

    
    def Work(self, player):
        if self.moveDis != self.tarDis:
            self.on = True
            player.rect = player.rect.move(0, -self.velocity)


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

def scene_walls():
    image_wall = pygame.transform.scale( pygame.image.load(r".\assets_library\tiles\12.jpg"), (40, 40) )

    obstacles = []

    for i in range(2 * WindowSettings.width // 40 + 1):
        obstacles.append(Block(image_wall, SceneSettings.tileWidth * i, 760))
    
    for i in range(WindowSettings.width // 40 + 1, 2 * WindowSettings.width // 40 + 1):
        obstacles.append(Block(image_wall, SceneSettings.tileWidth * i, 640))
    

    for i in range(2 * WindowSettings.height // 40 + 1):
        obstacles.append(Block(image_wall, 1640, SceneSettings.tileWidth * i))
    return obstacles

def scene_machines():
    image_machine = pygame.transform.scale( pygame.image.load(r".\assets_library\tiles\Machine.jpg"), (40, 40) )

    machines = []

    machines.append(Machine(image_machine, 400, 720, 400))
    return machines

def level_walls():
    image_wall = pygame.transform.scale( pygame.image.load(r".\assets_library\tiles\12.jpg"), (40, 40) )
    walls = []

    for cord in level.Walls:
        walls.append(Block(image_wall, cord[0] * 40, cord[1] * 40))
    return walls

def level_machines():
    image_machine = pygame.transform.scale( pygame.image.load(r".\assets_library\tiles\Machine.jpg"), (40, 40) )

    machines = []

    machines.append(Machine(image_machine, 1600, 400, 240))
    return machines