import pygame
import sys
from pygame.locals import *
#---初始化pygame
pygame.init()
s = pygame.display.list_modes()
sise = width,height = 600,400           
bg = (0,0,0)


fullscreen = False             

screen = pygame.display.set_mode(sise,RESIZABLE)
#-设置标题
pygame.display.set_caption("初次见面多多关照")

#-加载图片
tutrtle = pygame.image.load("G:/PersonPro/PythonPro/每日任务/爬虫的自我修养/pygame/turtle4.png")
#-获得图像的矩形位置
position = tutrtle.get_rect()

speed = [5,0]
tutrtle_right = pygame.transform.rotate(tutrtle,90)
tutrtle_top = pygame.transform.rotate(tutrtle,180)
tutrtle_left = pygame.transform.rotate(tutrtle,270)
tutrtle_bottom = tutrtle
tutrtle = tutrtle_top

l_head = tutrtle
r_head = pygame.transform.flip(tutrtle,True,False)
isquit = False
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            isquit = True
            break
        if event.type == KEYDOWN:
            #---全屏(F11)
            if event.key == K_q:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((1366,768),FULLSCREEN | HWSURFACE)
                else:
                    screen = pygame.display.set_mode(sise,RESIZABLE)

    # if isquit:
    #     break

    #------移动图像
    position = position.move(speed)#-----是如何让将一张图像到另一张图像上去的

    if position.right > width:
        tutrtle = tutrtle_right
        position = tutrtle_rect = tutrtle.get_rect()
        position.left = width - tutrtle_rect.width
        speed = [0,5]
    if position.bottom > height:
        tutrtle = tutrtle_bottom
        position = tutrtle_rect =tutrtle.get_rect()
        position.left = width - tutrtle_rect.width
        position.top = height - tutrtle_rect.height
        speed = [-5,0]
    if position.left < 0:
        tutrtle = tutrtle_left
        position = tutrtle_rect =tutrtle.get_rect()
        position.top = height - tutrtle_rect.height
        speed = [0,-5]
    if position.top < 0:
        tutrtle = tutrtle_top
        position = tutrtle_rect =tutrtle.get_rect()
        speed = [5,0]        
        

    #填充背景
    screen.fill(bg)
    #更新图像
    screen.blit(tutrtle,position)
    #更新界面
    pygame.display.flip()
    #延迟10毫秒
    pygame.time.delay(10)
    #clock.tick(200)
