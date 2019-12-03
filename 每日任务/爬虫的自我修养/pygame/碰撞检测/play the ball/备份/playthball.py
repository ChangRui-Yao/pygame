import pygame
import sys
import traceback
from pygame.locals import *
from random import *

#--球继承自Spite类
class Ball(pygame.sprite.Sprite):
    def __init__(self,grayball_image,greenball_image,position,speed,bg_size,target):
        #-初始化动画精灵
        pygame.sprite.Sprite.__init__(self)

        self.grayball_image = pygame.image.load(grayball_image).convert_alpha()
        self.greenball_image = pygame.image.load(greenball_image).convert_alpha()
        self.rect = self.grayball_image.get_rect()
        #--将小球指定位置
        self.rect.left,self.rect.top = position
        self.side = [choice([-1,1]),choice([-1,1])]
        self.speed = speed
        self.collide = False
        self.target = target#----鼠标事件要达成的目标
        self.control = False
        self.width,self.height = bg_size[0],bg_size[1]
        self.radius = self.rect.width / 2
    
    def move(self):
        if self.control:#---如果是玩家控制  则取原来的算法
            self.rect = self.rect.move(self.speed)
        else:               #---电脑的话 带加速度
            self.rect = self.rect.move(self.side[0] * self.speed[0],\
                self.side[1] * self.speed[1])      #--获得移动效果
        #-----如果小球的左侧出了边界，那么将小球的左侧改为右侧的边界
        #-----这样便实现了   从左边进入 从右边出来的效果
        if self.rect.right <= 0:
            self.rect.left = self.width

        elif self.rect.left >= self.width:
            self.rect.right = 0

        elif self.rect.bottom <= 0 :
            self.rect.top = self.height

        elif self.rect.top >= self.height:
            self.rect.bottom = 0
    def check(self,motion):
        if self.target < motion < self.target + 5:
            return True
        else:
            return False



class Glass(pygame.sprite.Sprite):
    def __init__(self,glass_image,mouse_image,bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.glass_image = pygame.image.load(glass_image).convert_alpha()
        self.glass_rect = self.glass_image.get_rect()
        self.glass_rect.left, self.glass_rect.top =\
            (bg_size[0] - self.glass_rect.width) // 2,\
                (bg_size[1] - self.glass_rect.height)
        self.mouse_image = pygame.image.load(mouse_image).convert_alpha()
        self.mouse_rect = self.mouse_image.get_rect()
        self.mouse_rect.left, self.mouse_rect.top = \
            self.glass_rect.left ,self.glass_rect.top
        pygame.mouse.set_visible(False)#--定义原始鼠标指真不可见




def main():
    pygame.init()

    grayball_image = "G:\\PersonPro\\PythonPro\\每日任务\\爬虫的自我修养\\pygame\\碰撞检测\\play the ball\\gray_ball.png"
    greenball_image = "G:\\PersonPro\\PythonPro\\每日任务\\爬虫的自我修养\\pygame\\碰撞检测\\play the ball\\green_ball.png"
    glass_image = "G:\\PersonPro\\PythonPro\\每日任务\\爬虫的自我修养\\pygame\\碰撞检测\\play the ball\\glass(1).png"
    mouse_image = "G:\\PersonPro\\PythonPro\\每日任务\\爬虫的自我修养\\pygame\\碰撞检测\\play the ball\\hand.png"
    bg_image = "G:\\PersonPro\\PythonPro\\每日任务\\爬虫的自我修养\\pygame\\碰撞检测\\play the ball\\background.png"
    
    running = True
    #---添加背景音乐
    pygame.mixer_music.load("G:/PersonPro/PythonPro/每日任务/爬虫的自我修养/pygame/碰撞检测/bg_music.ogg")
    pygame.mixer_music.play()
    
    #----添加音效
    loser_sound = pygame.mixer.Sound("G:/PersonPro/PythonPro/每日任务/爬虫的自我修养/pygame/碰撞检测/play the ball/loser.wav")#失败音效
    laugh_sound = pygame.mixer.Sound("G:/PersonPro/PythonPro/每日任务/爬虫的自我修养/pygame/碰撞检测/play the ball/金馆长的嘲笑.wav")
    winner_sound = pygame.mixer.Sound("G:/PersonPro/PythonPro/每日任务/爬虫的自我修养/pygame/碰撞检测/play the ball/winner.wav")
    hole_sound = pygame.mixer.Sound("G:/PersonPro/PythonPro/每日任务/爬虫的自我修养/pygame/碰撞检测/play the ball/hole.wav")

    #---背景音乐结束时 游戏结束
    GAMEOVER = USEREVENT            #--自定义用户事件1    音乐结束  返回事件GAMEOVER
    pygame.mixer_music.set_endevent(GAMEOVER)
        #--根据背景图片指定游戏尺寸

    bg_size = width,height = 1024,681
    screen = pygame.display.set_mode(bg_size)
    pygame.display.set_caption("Play the ball")

    background = pygame.image.load(bg_image).convert_alpha()

    hole =[(100,120,190,210),(220,230,385,400),(500,510,315,325),(680,700,190,200),(900,910,410,425)]


    msgs = []
    #--用于存放小球的列表
    balls = []
    group = pygame.sprite.Group()

    #创建五个小球
    for i in range(5):
        #位置随机  速度随机
        position = randint(0,width-100),randint(0,height-100)
        speed = [randint(1,10),randint(1,10)]                   #----每次形成一个位置随机  速度随机的球  把他添加到把balls里
        ball = Ball(grayball_image,greenball_image,position,speed,bg_size,5*(i+1))
        while pygame.sprite.spritecollide(ball,group,False,pygame.sprite.collide_circle):#-检测随机出生位置  出生位置重叠处BUG
            ball.rect.left,ball.rect.top = randint(0,width-100),randint(0,height-100)
        balls.append(ball)
        group.add(ball)
    
    glass = Glass(glass_image,mouse_image,bg_size)
    
    #----这里获得每秒钟 鼠标产生事件的次数
    motion = 0


    MYTIMER = USEREVENT + 1#--自定义用户事件2 每一秒中触发一次
    pygame.time.set_timer(MYTIMER,1000)

    pygame.key.set_repeat(100,100)#------set_repeat()两个参数 第一个是第一次发送事件的时间间隔  第二个是指定重复发送事件的间隔
                                    #----表示重复响应某事件  小球获得加速度
    
    clock = pygame.time.Clock()                 #--控制游戏帧率

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            elif event.type == GAMEOVER:        #--定义如果的到这个GAMEOVER 的消息   就播放输了音效 暂停两秒 嘲笑
                loser_sound.play()
                pygame.time.delay(2000)
                laugh_sound.play()
                running = False             #--结束绘制小球循环退出
            
            elif event.type == MYTIMER:
                if motion:
                    for each in group:
                        if each.check(motion):
                            each.speed =[0,0]
                            each.control = True
                    motion = 0

                
            elif event.type == MOUSEMOTION:
                motion += 1
            
            elif event.type == KEYDOWN:
                if event.key == K_w:
                    for each in group:
                        if each.control:
                            each.speed[1] -= 1
                if event.key == K_s:
                    for each in group:
                        if each.control:
                            each.speed[1] += 1                
                if event.key == K_a:
                    for each in group:
                        if each.control:
                            each.speed[0] -= 1
                if event.key == K_d:
                    for each in group:
                        if each.control:
                            each.speed[0] += 1
                if event.key == K_SPACE:
                    for each in group:
                        if each.control:
                            for i in hole:
                                if i[0] <= each.rect.left <= i[1] and \
                                    i[2] <= each.rect.top <= i[3]:
                                    hole_sound.play()
                                    each.speed = [0,0]
                                    group.remove(each)
                                    temp = balls.pop(balls.index(each))
                                    balls.insert(0,temp)
                                    hole.remove(i)
                                if not hole:
                                    pygame.mixer_music.stop()
                                    winner_sound.play()
                                    pygame.time.delay(3000)
                                    msg = pygame.image.load("G:/PersonPro/PythonPro/每日任务/爬虫的自我修养/pygame/碰撞检测/play the ball/然并卵.png").convert_alpha()
                                    msg_pos = (width - msg.get_width()) // 2,\
                                        (height - msg.get_height()) // 2
                                    msgs.append((msg,msg_pos))
                                    laugh_sound.play()
                                    


        screen.blit(background,(0,0))#---实例化背景  
        screen.blit(glass.glass_image,glass.glass_rect)#-实例化背景上的摩擦面板


        glass.mouse_rect.left,glass.mouse_rect.top = pygame.mouse.get_pos()#--设置小手跟随鼠标移动移动
        if glass.mouse_rect.left < glass.glass_rect.left:           #--如果鼠标左侧小于玻璃面板的左侧
            glass.mouse_rect.left = glass.glass_rect.left
        if glass.mouse_rect.left > glass.glass_rect.right - glass.mouse_rect.width:
            glass.mouse_rect.left = glass.glass_rect.right - glass.mouse_rect.width
        if glass.mouse_rect.top < glass.glass_rect.top:
            glass.mouse_rect.top = glass.glass_rect.top
        if glass.mouse_rect.bottom > glass.glass_rect.bottom - glass.mouse_rect.height:
            glass.mouse_rect.bottom = glass.glass_rect.bottom - glass.mouse_rect.height

        screen.blit(glass.mouse_image,glass.mouse_rect)


        for each in balls:#-检测碰撞        
            each.move()
            if each.collide:#---默认 collide等于false   检测到碰撞   充新move 离开  获得随机加速度
                each.speed = [randint(1,10),randint(1,10)]
                each.collide =False
            if each.control:#----如果满足事件  画一个绿色的小球
                screen.blit(each.greenball_image,each.rect)
            else:
                screen.blit(each.grayball_image,each.rect)
        
        for each in group:
            group.remove(each)
            
            if pygame.sprite.spritecollide(each,group,False,pygame.sprite.collide_circle):
                each.side[0] = -each.side[0]
                each.side[1] = -each.side[1]
                each.collide = True
                if each.control:
                    each.side[0] = -1
                    each.side[1] = -1

                    each.control = False#-----表示小球只要受到碰撞就会失去控制
            
            
            group.add(each)
        for msg in msgs:
            screen.blit(msg[0],msg[1])
        pygame.display.flip()
        clock.tick(30)






if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()



