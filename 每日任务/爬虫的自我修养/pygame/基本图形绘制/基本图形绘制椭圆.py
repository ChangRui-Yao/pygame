#基本图形绘制之椭圆
#ellipse(Surface,color,Rect,width=0)
            #--第一个参数  指定绘制位置
            #--第二个参数  指定椭圆颜色
            #--第三个参数 指定矩形来绘制  这个举行被称之为限定矩形 如果限定矩形是正方形   绘制出来就是个圆形咯
            #--第四个参数  指定椭圆边框的大小 0的话表示填充这个椭圆  1或者1以上的话表示用第二个参数填充的颜色绘制他的边框

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


clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:#--判断退出
            sys.exit()
        
        
    
    screen.fill(WHITE)

    pygame.draw.ellipse(screen,BLACK,(100,100,440,100),0)
    pygame.draw.ellipse(screen,RED,(220,50,200,200),0)


    pygame.display.flip()


    clock.tick(120)