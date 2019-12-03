import pygame
from random import *
class Bullet_Supply(pygame.sprite.Sprite):
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("G:/PersonPro/PythonPro/每日任务/爬虫的自我修养/pygame/飞机大战/images/bullet_supply.png").convert_alpha()
        self.rect = self.image.get_rect()
    
        self.width,self.height = bg_size[0],bg_size[1]

        self.rect.left,self.rect.bottom = randint(0,self.width - self.rect.width),-100#--初始化位置
        self.speed = 5#---移动速度
        self.active = False#--判断活着
        self.mask = pygame.mask.from_surface(self.image)#--完美检测

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.active = False
    def reset(self):
        self.active = True
        self.rect.left,self.rect.bottom = randint(0,self.width - self.rect.width),-100#--初始化位置


class Bomb_Supply(pygame.sprite.Sprite):
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("G:/PersonPro/PythonPro/每日任务/爬虫的自我修养/pygame/飞机大战/images/bomb_supply.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.width,self.height = bg_size[0],bg_size[1]

        self.rect.left,self.rect.bottom = randint(0,self.width - self.rect.width),-100#--初始化位置
        self.speed = 5#---移动速度
        self.active = False#--判断活着
        self.mask = pygame.mask.from_surface(self.image)#--完美检测

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.active = False
    def reset(self):
        self.active = True
        self.rect.left,self.rect.bottom = randint(0,self.width - self.rect.width),-100#--初始化位置