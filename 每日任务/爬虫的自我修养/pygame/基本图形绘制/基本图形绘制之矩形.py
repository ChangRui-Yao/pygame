#绘制矩形
#-------rect(Surface，color，Rect，width=0)
            #-第一个参数绘制在那个对象上
            #-第二个参数指定矩形的颜色
            #-指定矩形的范围
            #-指定矩形边框的大小 0的话表示填充这个矩形  1或者1以上的话表示用第二个参数填充的颜色绘制他的边框
import pygame
import sys
from pygame.locals import *


pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)


size = width,height = 640,480
screen = pygame.display.set_mode(size)
pygame.display.set_caption("绘制矩形")


clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        
    
    screen.fill(WHITE)

    pygame.draw.rect(screen,BLACK,(50,50,150,50),0)
    pygame.draw.rect(screen,BLACK,(250,50,150,50),1)
    pygame.draw.rect(screen,BLACK,(450,50,150,50),10)

    pygame.display.flip()


    clock.tick(10)