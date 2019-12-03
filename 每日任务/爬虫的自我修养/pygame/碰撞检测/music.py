import pygame
import sys
from pygame.locals import *

pygame.init()                           #--初始化这两个模块
pygame.mixer.init()

pygame.mixer_music.load("G:/PersonPro/PythonPro/每日任务/爬虫的自我修养/pygame/碰撞检测/bg_music.ogg")
pygame.mixer.music.set_volume(0.2)              #--加载背景音乐  设置音量
pygame.mixer.music.play()


cat_sound = pygame.mixer.Sound("G:\\PersonPro\\PythonPro\\每日任务\\爬虫的自我修养\\pygame\\碰撞检测\\猫叫.wav")
cat_sound.set_volume(0.2)
dog_sound = pygame.mixer.Sound("G:\\PersonPro\\PythonPro\\每日任务\\爬虫的自我修养\\pygame\\碰撞检测\\狗叫.wav")          #--加载音效设置音量
dog_sound.set_volume(0.2)


bg_size = width,height = 600,480
screen = pygame.display.set_mode(bg_size)           #-创建一个窗口
pygame.display.set_caption("猫狗大战")

pause = False
pause_image = pygame.image.load("G:\\PersonPro\\PythonPro\\每日任务\\爬虫的自我修养\\pygame\\碰撞检测\\暂停.png").convert_alpha()
unpause_image = pygame.image.load("G:\\PersonPro\\PythonPro\\每日任务\\爬虫的自我修养\\pygame\\碰撞检测\\蝙蝠侠.png").convert_alpha()
pause_rect = pause_image.get_rect()
pause_rect.left,pause_rect.top = (width-pause_rect.width) // 2,(height - pause_rect.height) // 2

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                cat_sound.play()
            if event.button == 3:
                dog_sound.play()
        
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                pause = not pause

    screen.fill((255,255,255))


    if pause:
        screen.blit(pause_image,pause_rect)
        pygame.mixer.music.pause()

    else:
        screen.blit(unpause_image,pause_rect)
        pygame.mixer.music.unpause()

    pygame.display.flip()
    clock.tick(30)      

