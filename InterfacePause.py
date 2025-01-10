import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption('Pause')
clock = pygame.time.Clock()
#以上为初始化

'''这是暂停页面，没有背景'''

'''README
运行后有四个图像
正中间： 继续游戏
左下： 重新开始
中下： 操作方法，就是不知道哪个按键是哪个的话就点这个
右下： 退出游戏'''

'''从这里找有用的
    正片开始'''
test_color = 'Pink'   #字体颜色统一，我先搞成粉色

#这是Pause文字
Pause_font = pygame.font.Font(None, 100)
Pause_surf = Pause_font.render('PAUSE', False, test_color).convert_alpha()
Pause_rect = Pause_surf.get_rect(center = (500, 150))

#这是Continue图像和文字
continue_surf = pygame.image.load('assets_library\特殊符号\continue.png').convert_alpha()
continue_surf= pygame.transform.scale(continue_surf, (150, 150))
continue_rect = continue_surf.get_rect(center = (500, 350))

Continue_font = pygame.font.Font(None, 50)
Continue_surf = Continue_font.render('continue', False, test_color).convert_alpha()
Continue_rect = Continue_surf.get_rect(center = (500, 450))

#这是Replay的图像和文字
replay_surf = pygame.image.load('assets_library\特殊符号\\replay.png').convert_alpha()
replay_surf= pygame.transform.scale(replay_surf, (80, 80))
replay_rect = replay_surf.get_rect(center = (200, 575))

Restart_font = pygame.font.Font(None, 50)
Restart_surf = Restart_font.render('restart', False, test_color).convert_alpha()
Restart_rect = Restart_surf.get_rect(center = (200, 650))

#这是Question的图像和文字
question_surf = pygame.image.load('assets_library\特殊符号\\question.png').convert_alpha()
question_surf= pygame.transform.scale(question_surf, (80, 80))
question_rect = replay_surf.get_rect(center = (500, 575))

Question_font = pygame.font.Font(None, 50)
Question_surf = Question_font.render('questions', False, test_color).convert_alpha()
Question_rect = Question_surf.get_rect(center = (500, 650))

#这是Home的图像和文字
home_surf = pygame.image.load('assets_library\特殊符号\\Home.png').convert_alpha()
home_surf= pygame.transform.scale(home_surf, (80, 80))
home_rect = replay_surf.get_rect(center = (800, 575))

Home_font = pygame.font.Font(None, 50)
Home_surf = Home_font.render('Quit', False, test_color).convert_alpha()
Home_rect = Home_surf.get_rect(center = (800, 650))

while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    #把上面的东西都画出来
    screen.blit(Pause_surf, Pause_rect)
    screen.blit(continue_surf, continue_rect)
    screen.blit(Continue_surf, Continue_rect)
    screen.blit(replay_surf, replay_rect)
    screen.blit(Restart_surf, Restart_rect)
    screen.blit(question_surf, question_rect)
    screen.blit(Question_surf, Question_rect)
    screen.blit(home_surf, home_rect)
    screen.blit(Home_surf, Home_rect)
    '''正片结束'''

    pygame.display.update()
    clock.tick(60)