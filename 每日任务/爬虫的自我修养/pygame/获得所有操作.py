import pygame
import sys
#---初始化pygame
pygame.init()

sise = width,height = 600,400
screen = pygame.display.set_mode(sise)#---------------在这里利用pygame的display创建了一个大小为sise的窗口
#---------设置窗口标题
pygame.display.set_caption("初次见面多多关照")
f = open("cerord.txt","w")




while True:
    for event in pygame.event.get():
        f.write(str(event) + "\n")

        if event.type == pygame.QUIT:
            f.close()
            sys.exit()
  