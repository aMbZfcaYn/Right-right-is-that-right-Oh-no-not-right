
import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption('Welcome!')
clock = pygame.time.Clock()
#以上为初始化


'''这是一开始的欢迎页面'''

'''README
点击 Press Here To Start! :) 后，玩家进入游戏页面'''
'''从这里找有用的
    正片开始'''
#这是背景
Bg_suef = pygame.image.load('assets_library\scenes\WelcomeBg.gif').convert_alpha()
Bg_suef= pygame.transform.scale(Bg_suef, (1000, 800))
Bg_rect = Bg_suef.get_rect(topleft = (0, 0))
#这是Welcome的文字
Welcome_font = pygame.font.Font(None, 150)
Welcome_surf = Welcome_font.render('Welcome!', False, 'Black').convert_alpha()
Welcome_rect = Welcome_surf.get_rect(center = (500, 300))
#这是Press Here To Start的文字
PressHere_font = pygame.font.Font(None, 100)
PressHere_surf = PressHere_font.render('Press Here To Start! :)', False, 'Black').convert_alpha()
PressHere_rect = PressHere_surf.get_rect(center = (500, 600))
#这是Press Here To Start下面的图案
bgPress_suef = pygame.image.load('assets_library\objects\\bg_for_PressHere.png').convert_alpha()
bgPress_suef= pygame.transform.scale(bgPress_suef, (880, 200))
bgPress_rect = bgPress_suef.get_rect(center = (500, 600))
#这是啥笔外星人的图案
alien_surf = pygame.image.load('assets_library\characters\外星人.png').convert_alpha()
alien_rect = alien_surf.get_rect(midbottom = (1200, 505))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #把上面的东西全都画出来
    screen.blit(Bg_suef, Bg_rect)
    screen.blit(Welcome_surf, Welcome_rect)
    alien_rect.left -= 4
    if alien_rect.right <= 0: alien_rect.left = 1000
    screen.blit(alien_surf, alien_rect)
    screen.blit(bgPress_suef, bgPress_rect)
    screen.blit(PressHere_surf, PressHere_rect)
    '''正片结束'''


    pygame.display.update()
    clock.tick(60)