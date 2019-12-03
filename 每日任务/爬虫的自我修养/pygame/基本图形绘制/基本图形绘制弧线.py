#基本图形绘制 弧线
#arc(surface,color,Rect,start_angle,stop_angle,width=1)
        #--第一个参数  指定绘制位置
        #--第二给参数  指定绘制颜色
        #--第三个参数 指定限定矩形来绘制 
        #--第四个参数   表示椭圆的那一部分开始  起始角度
        #--第五个参数  表示椭圆的那一部分结束   结束角度
        #--第六个参数  指定椭圆边框的大小 弧线是不能填充的
#-需要调用Π   不想调用  直接写3.14也行   import math
import pygame
import sys
import math
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

    pygame.draw.arc(screen,BLACK,(100,100,440,100),0,math.pi,1)
    pygame.draw.arc(screen,RED,(220,50,200,200),math.pi,math.pi*2,1)


    pygame.display.flip()


    clock.tick(120)