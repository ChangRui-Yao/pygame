#---基本图形绘制  圆形
#-----circle(Surface,color,pos,radius,width=0)
        #_第一个参数 指定制定那个位置绘制
        #-第二个参数  指定圆形的颜色
        #-第三个参数 指定圆心的位置
        #-第四个参数 指定半径的大小
        #-第五个参数 指定0的话表示填充这个圆形  1或者1以上的话表示用第二个参数填充的颜色绘制他的边框

import pygame
import sys
from pygame.locals import *


pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)


size = width,height = 640,480
screen = pygame.display.set_mode(size)
pygame.display.set_caption("绘制圆形")

position = size[0]//2,size[1]//2
moving = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:#--判断退出
            sys.exit()
        
        if event.type == MOUSEBUTTONDOWN:#--判断鼠标点下
            if event.button == 1:
                moving = True
        if event.type == MOUSEBUTTONUP:#--判断抬起
            if event.button == 1:
                moving = False
    if moving:
        position = pygame.mouse.get_pos()#-----把当前鼠标位置给这个圆心

        
    
    screen.fill(WHITE)

    pygame.draw.circle(screen,RED,position,25,1)
    pygame.draw.circle(screen,GREEN,position,75,1)
    pygame.draw.circle(screen,BLUE,position,125,1)


    pygame.display.flip()


    clock.tick(120)