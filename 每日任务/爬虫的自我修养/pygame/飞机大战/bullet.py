import pygame

class Bullet1(pygame.sprite.Sprite):
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("G:/PersonPro/PythonPro/每日任务/爬虫的自我修养/pygame/飞机大战/images/bullet1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = position

        self.speed = 12         #--子弹速度略快于飞机速度
        self.active = False        #-子弹活着
        self.mask = pygame.mask.from_surface(self.image)                   #--用于完美检测


    def move(self):
        self.rect.top -= self.speed


        if self.rect.top < 0:
            self.active = False

    def reset(self,position):
        self.rect.left,self.rect.top = position
        self.active = True

class Bullet2(pygame.sprite.Sprite):
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("G:/PersonPro/PythonPro/每日任务/爬虫的自我修养/pygame/飞机大战/images/bullet2.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = position

        self.speed = 14         #--子弹速度略快于飞机速度
        self.active = False        #-子弹活着
        self.mask = pygame.mask.from_surface(self.image)                   #--用于完美检测


    def move(self):
        self.rect.top -= self.speed


        if self.rect.top < 0:
            self.active = False

    def reset(self,position):
        self.rect.left,self.rect.top = position
        self.active = True