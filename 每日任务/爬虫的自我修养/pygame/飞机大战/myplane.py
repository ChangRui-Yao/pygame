import pygame

class MyPlane(pygame.sprite.Sprite):
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image1 = pygame.image.load("G:/PersonPro/PythonPro/每日任务/爬虫的自我修养/pygame/飞机大战/images/me1.png").convert_alpha()
        self.image2 = pygame.image.load("G:/PersonPro/PythonPro/每日任务/爬虫的自我修养/pygame/飞机大战/images/me2.png").convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load("G:/PersonPro/PythonPro/每日任务/爬虫的自我修养/pygame/飞机大战/images/me_destroy_1.png").convert_alpha(),\
                pygame.image.load("G:/PersonPro/PythonPro/每日任务/爬虫的自我修养/pygame/飞机大战/images/me_destroy_2.png").convert_alpha(),\
                    pygame.image.load("G:/PersonPro/PythonPro/每日任务/爬虫的自我修养/pygame/飞机大战/images/me_destroy_3.png").convert_alpha(),\
                        pygame.image.load("G:/PersonPro/PythonPro/每日任务/爬虫的自我修养/pygame/飞机大战/images/me_destroy_4.png").convert_alpha()\
                            ])
        self.rect = self.image1.get_rect()
        self.width,self.height = bg_size[0],bg_size[1]
        self.rect.left,self.rect.top = \
            (self.width - self.rect.width) // 2,\
                self.height - self.rect.height - 60

        self.speed = 10
        self.wudi = False
        self.active =True
        self.mask = pygame.mask.from_surface(self.image1)#--用pygame里的mask模块里的这个surface  将传进来的这个image的非透明部分标记为mask
                                                        #—每个对象必须有这个mask属性  它用于得到检测的范围


    def moveUP(self):
        if self.rect.top > 0:
            self.rect.top -= self.speed
        else:
            self.rect.top = 0
    def moveDOWN(self):
        if self.rect.bottom < self.height - 60:
            self.rect.top += self.speed
        else:
            self.rect.bottom = self.height - 60
    def moveLEFT(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0
    def moveRIGHT(self):
        if self.rect.right < self.width:
            self.rect.left += self.speed
        else:
            self.rect.right = self.width
        
    def reset(self):
        self.rect.left,self.rect.top = \
            (self.width - self.rect.width) // 2,\
                self.height - self.rect.height - 60
        self.active = True
        self.wudi = True