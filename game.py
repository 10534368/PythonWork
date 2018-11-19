import pygame
from pygame.locals import *
from sys import exit

pygame.init()
background_image = '11.jpg'
mouse_image = 'basic.cur'

screen = pygame.display.set_mode((1366,768),0, 32)
pygame.display.set_caption("地下城与勇士")
background = pygame.image.load(background_image).convert()
mouse_cursor = pygame.image.load(mouse_image).convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:  # 接收到退出事件后退出程序
            exit()
        elif event.type==KEYDOWN:
            if event.key==K_SPACE:
                exit()
    screen.blit(background, (0, 0))  # 画上背景图

    x, y = pygame.mouse.get_pos()  # 获得鼠标位置
    # 计算光标左上角位置
    x -= mouse_cursor.get_width()/2
    y -= mouse_cursor.get_height()/2
    # 画上光标
    screen.blit(mouse_cursor, (x, y))

    # 刷新画面
    pygame.display.update()