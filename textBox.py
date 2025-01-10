import pygame
import sys

from Settings import *

pygame.init()

window = pygame.display.set_mode((WindowSettings.width, WindowSettings.height))

# 文本框的位置和大小
input_box_x = 100
input_box_y = 100
input_box_width = 400
input_box_height = 50

# 文本框的颜色
input_box_color = (255, 255, 255)  # 白色
input_box_border_color = (0, 0, 0)  # 黑色

# 文本的字体和颜色
font = pygame.font.Font(None, 32)
text_color = (0, 0, 0)  # 黑色

# 初始化文本内容
text = ''

def draw_input_box(window, x, y, width, height, color, border_color, text, font, text_color):
    # 绘制文本框背景
    pygame.draw.rect(window, color, (x, y, width, height))
    # 绘制文本框边框
    pygame.draw.rect(window, border_color, (x, y, width, height), 2)
    # 渲染文本
    text_surface = font.render(text, True, text_color)
    # 绘制文本
    window.blit(text_surface, (x + 5, y + 5))

active = False  # 文本框是否被激活

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # 检查鼠标点击位置是否在文本框内
            if input_box_x <= event.pos[0] <= input_box_x + input_box_width and \
               input_box_y <= event.pos[1] <= input_box_y + input_box_height:
                active = not active
            else:
                active = False
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                elif event.key == pygame.K_RETURN:
                    print(text)  # 处理输入的文本
                    text = ''
                else:
                    text += event.unicode

    # 填充背景
    window.fill((200, 200, 200))

    # 绘制文本框
    draw_input_box(window, input_box_x, input_box_y, input_box_width, input_box_height,
                   input_box_color, input_box_border_color, text, font, text_color)

    # 更新显示
    pygame.display.flip()

    # 控制帧率
    pygame.time.Clock().tick(30)

