# #--plgame  给定当前的基类
  #碰撞检测                       spritecollide(sqrite,group,dokill,collided = None)
    #-第一个参数 指定被检测的精灵
   #-第二个参数 指定一个阻    要用sprite.Group()生成阻
   #-第三个参数 设置是否从阻中删除阻中检测到碰撞的精灵  如果设置为Ture  他会把检测阻中到碰撞的精灵删掉
#-第四个参数  制定一个回调函数  他是用于定制特殊的检测方法 如果第四个参数忽略的话 默认检测精灵之间的rect属性
#---

#----因为小球 的图标并不是圆的  也是一部分的正方体  有的角度碰撞 会显示 明明没有碰到  但是还是改变方向了
#--这个sprite模块里 有一个collide_circle(left,right)的模块  用与检测两个圆的碰撞
                #--两个参数 分别是两个精灵    
                # 不过这个需要一个叫半径的属性    self.radius  在这里 直接将这个模块作为 碰撞检测的第四个参数处传进去
#-----每个黑洞的范围     （x1,x2,y1,y2）    hole = [(117,119,199,201),(225,227,390,392),(503,505,320,322),(698,700,192,194),(906,908,419,421)]
import pygame1
import sys
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
        self.speed = speed
        self.target = target#----鼠标事件要达成的目标
        self.control = False
        self.width,self.height = bg_size[0],bg_size[1]
        self.radius = self.rect.width / 2
    
    def move(self):
        self.rect = self.rect.move(self.speed)      #--获得移动效果
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
    #--用于存放小球的列表
    balls = []
    group = pygame.sprite.Group()

    #创建五个小球
    for i in range(5):
        #位置随机  速度随机
        position = randint(0,width-100),randint(0,height-100)
        speed = [randint(-10,10),randint(-10,10)]                   #----每次形成一个位置随机  速度随机的球  把他添加到把balls里
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
            if each.control:#----如果满足事件  画一个绿色的小球
                screen.blit(each.greenball_image,each.rect)
            else:
                screen.blit(each.grayball_image,each.rect)
        
        for each in group:
            group.remove(each)
            
            if pygame.sprite.spritecollide(each,group,False,pygame.sprite.collide_circle):
                each.speed[0] = -each.speed[0]
                each.speed[1] = -each.speed[1]
                each.control = False#-----表示小球只要受到碰撞就会失去控制
            
            
            group.add(each)

        pygame.display.flip()
        clock.tick(30)






if __name__ == "__main__":
    main()
