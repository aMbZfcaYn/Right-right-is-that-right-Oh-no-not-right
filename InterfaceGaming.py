import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption('Welcome!')
clock = pygame.time.Clock()
#以上为初始化

'''这是游戏过程中的页面，没有背景，直接画在游戏界面上面就行了'''

'''README
运行后有两个图像
左上角： 生命值，鼠标点了没有反应
右上角： 暂停，鼠标点了后出现暂停页面，也就是InterfacsPause中的东西
中间那个是我在瞎搞'''

'''从这里找有用的
    正片开始'''
test_color = 'Pink'   #字体颜色统一，我先搞成粉色
heart_amount = 5   #剩下的生命值，我先设成5

#这是Pause图像和文字
pause_surf = pygame.image.load('assets_library\特殊符号\pause.png').convert_alpha()
pause_surf= pygame.transform.scale(pause_surf, (40, 40))
pause_rect = pause_surf.get_rect(center = (955, 45))

Pause_font = pygame.font.Font(None, 30)
Pause_surf = Pause_font.render('pause', False, test_color).convert_alpha()
Pause_rect = Pause_surf.get_rect(center = (955, 80))

#这是Heart图像和文字，还有冒号和数字
heart_surf = pygame.image.load('assets_library\特殊符号\heart.png').convert_alpha()
heart_surf= pygame.transform.scale(heart_surf, (40, 40))
heart_rect = heart_surf.get_rect(center = (45, 45))

Heart_font = pygame.font.Font(None, 30)
Heart_surf = Heart_font.render('Heart', False, test_color).convert_alpha()
Heart_rect = Heart_surf.get_rect(center = (45, 80))

heart_amount_font = pygame.font.Font(None, 50)
heart_amount_surf = heart_amount_font.render(f": {heart_amount}", False, test_color).convert_alpha()
heart_amount_rect = heart_amount_surf.get_rect(center = (90, 45))

#这是中间的 Have Fun! :)
HaveFun_font = pygame.font.Font(None, 80)
HaveFun_surf = HaveFun_font.render('Have Fun! :)', False, test_color).convert_alpha()
HaveFun_rect = HaveFun_surf.get_rect(center = (500, 50))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEMOTION:
            print(event.pos)

    screen.blit(pause_surf, pause_rect)
    screen.blit(Pause_surf, Pause_rect)
    screen.blit(heart_surf, heart_rect)
    screen.blit(Heart_surf, Heart_rect)
    screen.blit(heart_amount_surf, heart_amount_rect)
    screen.blit(HaveFun_surf, HaveFun_rect)
    '''正片结束'''

    pygame.display.update()
    clock.tick(60)