#-------多边形绘制
#------polygon(Surface,color,pointlist,width=0)
        #第一个参数 指定在哪里绘制
        #-第二个参数制定绘制颜色
        #--第三个参数制定多边形每个顶点坐标hi相连接的列表
        #--第四个参数 指定多边形边框的大小 0的话表示填充这个矩形  1或者1以上的话表示用第二个参数填充的颜色绘制他的边框
import pygame
import sys
from pygame.locals import *


pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)

points = [(200,75),(300,25),(400,75),(450,25),(450,125),(400,75),(300,125),]


size = width,height = 640,480
screen = pygame.display.set_mode(size)
pygame.display.set_caption("绘制多边形")


clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        
    
    screen.fill(WHITE)

    pygame.draw.polygon(screen,GREEN,points,0)

    pygame.display.flip()


    clock.tick(10)