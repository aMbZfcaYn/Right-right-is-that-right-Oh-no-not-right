import pygame
from Settings import *
from LevelMap import *
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
    def __init__(self, image, x, y, dis, dir: str):
        super().__init__(image, x, y)
        self.tarDis = dis
        self.dir = dir
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
        if self.moveDis == 0:
            self.stayTick = 30 * self.stayTime
            self.returning = False
        
        self.move()

    def move(self):
        if self.returning:
            self.moveDis -= self.velocity * 2
            if self.dir == "UP": self.rect = self.rect.move(0, self.velocity * 2)
            if self.dir == "DOWN": self.rect = self.rect.move(0, self.velocity * -2)
            if self.dir == "LEFT": self.rect = self.rect.move(self.velocity * 2, 0)
            if self.dir == "RIGHT": self.rect = self.rect.move(self.velocity * -2, 0)
        if self.on:
            self.moveDis += self.velocity
            if self.dir == "UP": self.rect = self.rect.move(0, -self.velocity)
            if self.dir == "DOWN": self.rect = self.rect.move(0, self.velocit)
            if self.dir == "LEFT": self.rect = self.rect.move(-self.velocity, 0)
            if self.dir == "RIGHT": self.rect = self.rect.move(self.velocity, 0)
                
    def Work(self, player):
        if self.moveDis == 0: self.on = True
        player.rect.bottom = self.rect.top
        if self.on:
            if self.dir == "LEFT": player.rect = player.rect.move(-self.velocity, 0)
            if self.dir == "RIGHT": player.rect = player.rect.move(self.velocity, 0)
        if self.returning:
            if self.dir == "LEFT": player.rect = player.rect.move(2 * self.velocity, 0)
            if self.dir == "RIGHT": player.rect = player.rect.move(-2 * self.velocity, 0)

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

class Enemy(Anim):
    def __init__(self, image, x, y, actDis: int):
        super().__init__(image, x, y)
        self.actDis = actDis
        self.moveDis = 0
        self.isDead = False
        #move info
        self.velocity = 5
        self.facingRight = True
        self.facingDir = 1
    
    def update(self, player):
        super().update()
        self.image = pygame.transform.flip( self.image, self.facingRight, False )
        if ( self.moveDis == 0 and not self.facingRight ) or ( self.moveDis == self.actDis and self.facingRight ): self.flip()
        else: self.move()

    def flip(self):
        self.facingRight = not self.facingRight
        self.facingDir = -self.facingDir    
    
    def move(self):
        self.cord = ( self.cord[0] + self.velocity * self.facingDir, self.cord[1] )
        self.moveDis += self.velocity * self.facingDir

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

    machines.append(Machine(Images.machine, 400, 720, 400, "UP"))

    return machines

def scene_coins():
    coins = []
    coinsGot = []

    coins.append(Coin(Images.coin, 1000, 720, 20))
    coins.append(Coin(Images.coin, 400, 160, 20))
    coinsGot.append(True)

    return coins

def scene_enemies():
    enemies = []

    enemies.append(Enemy(Images.enemy, 1040, 600, 560))

    return enemies

def level_1_walls():
    walls = []
    for cord in level_1.Walls:
        walls.append(Block(Images.wall, cord[0] * 40, cord[1] * 40))
    return walls

def level_1_traps():
    traps = []
    for cord in level_1.Traps:
        traps.append(Trap(Images.trap, cord[0] * 40, cord[1] * 40 + 15))
    return traps

def level_1_machines():
    machines = []
    machines.append(Machine(Images.machine, 1600, 400, 240, "UP"))
    machines.append(Machine(Images.machine, 1320, 120, 400, "RIGHT"))
    return machines

def level_2_walls():
    walls = []
    for cord in level_2.Walls:
        walls.append(Block(Images.wall, cord[0] * 40, cord[1] * 40))
    return walls

def level_2_traps():
    traps = []
    for cord in level_2.Traps:
        traps.append(Trap(Images.trap, cord[0] * 40, cord[1] * 40 + 15))
    return traps

def level_2_enemies():
    enemies = []
    enemies.append(Enemy(Images.enemy, 40 * SceneSettings.tileWidth, 30 * SceneSettings.tileHeight, 320))
    enemies.append(Enemy(Images.enemy, 40 * SceneSettings.tileWidth, 27 * SceneSettings.tileHeight, 80))
    enemies.append(Enemy(Images.enemy, 28 * SceneSettings.tileWidth, 26 * SceneSettings.tileHeight, 240))
    enemies.append(Enemy(Images.enemy, 25 * SceneSettings.tileWidth, 23 * SceneSettings.tileHeight, 200))
    enemies.append(Enemy(Images.enemy, 28 * SceneSettings.tileWidth, 20 * SceneSettings.tileHeight, 240))
    return enemies

def level_2_machines():
    machines = []
    machines.append(Machine(Images.machine, 7 * SceneSettings.tileWidth, 10 * SceneSettings.tileHeight, 280, "UP"))
    machines.append(Machine(Images.machine, 73 * SceneSettings.tileWidth, 17 * SceneSettings.tileHeight, 120, "UP"))
    machines.append(Machine(Images.machine, 78 * SceneSettings.tileWidth, 34 * SceneSettings.tileWidth, 400, "LEFT"))
        
    return machines