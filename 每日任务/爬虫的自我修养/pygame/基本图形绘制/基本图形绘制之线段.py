#-基本图形绘制之线段
#这里有两种方法
                    # 1绘制一条线段line(surface,colar,start_pos,end_pos,width=1)
                            #-第一个参数 指定绘制位置
                            #--第二个参数 指定颜色
                            #--第三个参数 


                    #2绘制多条线段lines(surface,color,closed,pointlist,width=1)

                            #--第三个参数  closed如果设置为True或者为1   表示你画出来的线段是首尾相连的
                            # --第四个参数  列表
                            # --width不管设置为多少   线段都是不能填充的  如果等于0 线段不显示 所以不能等于0

            #1绘制抗锯齿的线段 
            #1aaline(surface,colar,startpos,endpos,blend=1)
                            #---第五个参数   blend指定是否通过绘制混合背景的阴影来实现抗锯齿功 1 开启 2 关闭

            #-2
            # aalines(surface,color,closed,pointlist,blend=1)
import pygame
import sys
from pygame.locals import *


pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)

points = [(200,75),(300,25),(400,75),(450,25),(450,125),(400,75),(300,125),]


size = width,height = 1020,600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("绘制线段")


clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        
    
    screen.fill(WHITE)

    pygame.draw.lines(screen,GREEN,1,points,1)
    pygame.draw.line(screen,BLACK,(100,200),(540,250),1)
    pygame.draw.aaline(screen,BLACK,(100,250),(540,300),1)
    pygame.draw.aaline(screen,BLACK,(100,300),(540,350),0)

    pygame.display.flip()


    clock.tick(10)
                            