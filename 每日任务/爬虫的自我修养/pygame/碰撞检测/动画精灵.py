#----所谓动画精灵  就是那些在游戏开发中  被赋予灵魂的事物  比如 小老鼠
#--面向对象的游戏开发思维
#--#--1体验游戏开发过程  
    #2碰撞检测      
    #                       spritecollide(sqrite,group,dokill,collided = None)
                            #-第一个参数 指定被检测的精灵
                            #-第二个参数 指定一个阻    要用sprite.Group()生成阻
                            #-第三个参数 设置是否从阻中删除阻中检测到碰撞的精灵  如果设置为Ture  他会把检测阻中到碰撞的精灵删掉
                            #-第四个参数  制定一个回调函数  他是用于定制特殊的检测方法 如果第四个参数忽略的话 默认检测精灵之间的rect属性
    #3异常处理
    #4计时器
    #5自定义事件
    #6播放声音
    #7替换鼠标样式
    #8限制鼠标移动范围
import pygame
import sys
import math
from pygame.locals import *
from random import *

class Ball(pygame.sprite.Sprite):
    def __init__(self,image,position,speed,bg_size):
        #-初始化动画精灵
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        #--将小球指定位置
        self.rect.left,self.rect.top = position
        self.speed = speed
        self.width,self.height = bg_size[0],bg_size[1]
    
    def move(self):
        self.rect = self.rect.move(self.speed)      #--获得加速度移动效果
        #-----如果小球的左侧出了边界，那么将小球的左侧改为右侧的边界
        #-----这样便实现了   从左边进入 从右边出来的效果
        if self.rect.right < 0:
            self.rect.left = self.width

        elif self.rect.left > self.width:
            self.rect.right = 0

        elif self.rect.bottom < 0 :
            self.rect.top = self.height

        elif self.rect.top > self.height:
            self.rect.bottom = 0


def collide_cheak(item,target):
    col_balls = []
    for each in target:
        distance = math.sqrt(\
            math.pow((item.rect.center[0] - each.rect.center[0]),2) +\
                 math.pow((item.rect.center[1] - each.rect.center[1]),2))
        if distance <= (item.rect.width + each.rect.width) / 2:
            col_balls.append(each)
    return col_balls


def main():
    pygame.init()

    ball_image = "G:\\PersonPro\\PythonPro\\每日任务\\爬虫的自我修养\\pygame\\碰撞检测\\play the ball\\gray_ball.png"
    bg_image = "G:\\PersonPro\\PythonPro\\每日任务\\爬虫的自我修养\\pygame\\碰撞检测\\play the ball\\background.png"
    
    running = True

        #--根据背景图片指定游戏尺寸
    bg_size = width,height = 1024,681
    screen = pygame.display.set_mode(bg_size)
    pygame.display.set_caption("Play the ball")                 #-设置 标题  尺寸 


    background = pygame.image.load(bg_image).convert_alpha()
    balls = []
    BALL_NUM = 5
    for i in range(BALL_NUM):
        position = randint(0,width-100),randint(0,height-100)
        speed = [randint(-10,10),randint(-10,10)]                   #----每次形成一个位置随机  速度随机的球  把他添加到把balls里
        ball = Ball(ball_image,position,speed,bg_size)
        while collide_cheak(ball,balls):
            ball.rect.left,ball.rect.top = randint(0,width-100),randint(0,height-100)
        balls.append(ball)
    
    clock = pygame.time.Clock()                 #--控制游戏帧率


    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
        
        screen.blit(background,(0,0))

        for each in balls:
            each.move()
            screen.blit(each.image,each.rect)
        
        for i in range(BALL_NUM):
            item = balls.pop(i)

            if collide_cheak(item,balls):
                item.speed[0] = -item.speed[0]
                item.speed[1] = -item.speed[1]

            balls.insert(i,item)


        
        pygame.display.flip()
        clock.tick(30)



if __name__ == "__main__":
    main()