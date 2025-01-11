import pygame
from Settings import *
from LevelMap import level
from random import randint

# 静态场景：Block
class Block(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        '''self.lastCameraX = 0
        self.lastCameraY = 0'''

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
        
    def update(self, player):
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
            if self.rect.colliderect(player.rect): player.rect = player.rect.move(0, -self.velocity)
            self.moveDis += self.velocity

    
    def Work(self, player):
        if self.moveDis == 0: self.on = True

class Trap(Block):
    def __init__(self, image, x, y):
        super().__init__(image, x, y)

#有动画的场景：Anim
class Anim(pygame.sprite.Sprite):
    def __init__(self, images:list, x, y):
        self.images = images
        self.animTimer = 0
        self.animIndex = 0
        self.image = images[0]
        self.rect = self.image.get_rect()
        self.cord = (x, y)
        self.animationTime = 6

    def update(self):
        self.image = self.images[self.animIndex]
        self.rect.topleft = self.cord
        self.animTimer += 1
        if self.animTimer >= self.animationTime:
            self.animIndex += 1
            self.animTimer = 0
        if self.animIndex >= len(self.images): self.Reset()

    def Reset(self):
        self.animIndex = 0
        self.animTimer = 0

class Coin(Anim):
    def __init__(self, image, x, y, value):
        super().__init__(image, x, y)
        self.value = value
        self.isGot = False

    def update(self):
        super().update()


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
    obstacles = []

    for i in range(2 * WindowSettings.width // 40 + 1):
        obstacles.append(Block(Images.wall, SceneSettings.tileWidth * i, 760))
    
    for i in range(WindowSettings.width // 40 + 1, 2 * WindowSettings.width // 40 + 1):
        obstacles.append(Block(Images.wall, SceneSettings.tileWidth * i, 640))
    
    for i in range(2 * WindowSettings.height // 40 + 1):
        obstacles.append(Block(Images.wall, 1640, SceneSettings.tileWidth * i))

    return obstacles

def scene_machines():
    machines = []

    machines.append(Machine(Images.machine, 400, 720, 400))

    return machines

def scene_coins():
    coins = []
    coinsGot = []

    coins.append(Coin(Images.coin, 1000, 720, 20))
    coinsGot.append(True)

    return coins

def level_traps():
    traps = []

    for cord in level.Traps:
        traps.append(Trap(Images.trap, cord[0] * 40, cord[1] * 40))
    return traps

def level_walls():
    walls = []

    for cord in level.Walls:
        walls.append(Block(Images.wall, cord[0] * 40, cord[1] * 40))
    return walls

def level_machines():
    machines = []

    machines.append(Machine(Images.machine, 1600, 400, 240))
    return machines